import sys
import logging

import re
import json
import requests
from bs4 import BeautifulSoup

from typing import List, Set, Tuple, Dict, Optional


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


class Configuration:
    def __init__(self, config_path: str):
        self.config = self._load_config(config_path)

    def _load_config(self, path: str) -> dict:
        with open(path, "r") as file:
            return json.load(file)

    @property
    def user_agent(self) -> str:
        return self.config.get("user_agent", "")

    @property
    def start_url(self) -> str:
        return self.config.get("start_url", "")

    @property
    def email_regex(self) -> str:
        return self.config.get("email_regex", "")

    @property
    def timeout_interval(self) -> int:
        return self.config.get("timeout_interval", 10)

    @property
    def max_depth(self) -> int:
        return self.config.get("max_depth", 1)


class LinkExtractor:
    @staticmethod
    def extract_links(html: str) -> List[str]:
        try:
            soup = BeautifulSoup(html, "html.parser")
            return [
                tag["href"]
                for tag in soup.find_all("a", href=True)
                if tag["href"].startswith("http")
            ]
        except Exception as e:
            logger.error(f"Error extracting links: {e}")
            return []


class EmailExtractor:
    def __init__(self, regex_pattern: str):
        self.pattern = re.compile(regex_pattern)

    def extract_emails(self, html: str) -> List[str]:
        return self.pattern.findall(html)


class HTTPClient:
    def __init__(self, headers: Dict[str, str], timeout: int):
        self.headers = headers
        self.timeout = timeout

    def get(self, url: str) -> Optional[str]:
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"HTTP error for {url}: {e}")
            return None


class CrawlerGraph:
    def __init__(self):
        self.graph: Dict[str, List[str]] = {}
        self.email_map: Dict[str, List[str]] = {}

    def add_links(self, url: str, links: List[str]):
        self.graph[url] = links

    def add_emails(self, url: str, emails: List[str]):
        if emails:
            self.email_map[url] = emails

    def display_tree(self):
        def dfs(node: str, depth: int, visited: Set[str]):
            if node in visited:
                return
            visited.add(node)
            print("    " * depth + ("└── " if depth > 0 else "") + node)
            for child in self.graph.get(node, []):
                dfs(child, depth + 1, visited)

        print("\n Crawl Tree:")
        if self.graph:
            dfs(next(iter(self.graph)), 0, set())

    def display_emails(self):
        print("\n Email Tree:")
        for url, emails in self.email_map.items():
            print(f"└── {url}")
            for email in emails:
                print(f"    └── {email}")


class WebCrawler:
    def __init__(self, config: Configuration):
        self.config = config
        self.to_crawl: List[Tuple[str, int]] = [(config.start_url, 0)]
        self.crawled: Set[str] = set()
        self.emails: Set[str] = set()
        self.graph = CrawlerGraph()

        self.http_client = HTTPClient(
            headers={"User-Agent": config.user_agent}, timeout=config.timeout_interval
        )
        self.email_extractor = EmailExtractor(config.email_regex)

    def crawl(self):
        while self.to_crawl:
            url, depth = self.to_crawl.pop()
            if url in self.crawled or depth > self.config.max_depth:
                continue

            logger.info(f"Crawling (depth {depth}): {url}")
            html = self.http_client.get(url)
            if html is None:
                continue

            links = LinkExtractor.extract_links(html)
            self.graph.add_links(url, links)
            self.to_crawl.extend(
                (link, depth + 1) for link in links if link not in self.crawled
            )

            emails = self.email_extractor.extract_emails(html)
            self.graph.add_emails(url, emails)
            self.emails.update(emails)

            self.crawled.add(url)

        logger.info("Crawling complete !")
        logger.info(f"Crawled {len(self.crawled)} URLs")
        logger.info(f"Found {len(self.emails)} unique emails")
        self.graph.display_tree()
        self.graph.display_emails()


def main(config_path: str):
    config = Configuration(config_path)
    crawler = WebCrawler(config)
    crawler.crawl()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python email_finder_v2.py")
        sys.exit(1)
    main(sys.argv[1])
