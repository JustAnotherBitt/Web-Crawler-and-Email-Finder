# Web Crawler and Email Finder

## Description

This repository contains two Python scripts designed to run in terminal environments:

1. **Web Crawler**: A crawler that visits URLs, collects links, and extracts email addresses from web pages.
2. **Email Finder**: A script that analyzes web pages to find email addresses.

Both scripts can be executed from a terminal, with support for running in different environments.

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

## Instalation

1. Clone the repository:
`git clone <URL_DO_REPOSITORIO>`
   
2. Navigate to the project directory:
`cd <nome_do_diretorio>`

3. Make sure Python is installed on your system:

- Download: https://www.python.org/downloads/

4. Install the libraries:

- Requests: `pip install requests`
- BeautifulSoup: `pip install beautifulsoup4`

## Web Crawler

This script visits URLs, collects links, and extracts emails found on the pages.

### Example:

![image](https://github.com/user-attachments/assets/b82d854f-f8a4-431d-b7aa-c1dea56cc4d7)


### On PowerShell (Windows) with venv activated:

`.\.venv\Scripts\Activate`

`python web_crawler.py <URL>`

### On Terminal (Linux) without venv activated:

`python3 web_crawler.py <URL>`

## Email Finder

This script analyzes a web page to find and list email addresses.

### Example:

![image](https://github.com/user-attachments/assets/a2192bfc-6021-4c9c-a8c8-5a8fb3e1d958)


### On PowerShell (Windows) with venv activated:

`.\.venv\Scripts\Activate`

`python email_finder.py <URL>`

### On Terminal (Linux) without venv activated:

`python3 email_finder.py <URL>`

#### Notes:
- Replace <URL> with the URL of the page you want to analyze. The scripts will accept URLs and process the content as specified.
