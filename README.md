# Web Crawler e Email Finder

## Descrição

Este repositório contém dois scripts Python projetados para rodar em terminais:

1. **Web Crawler**: Um crawler que visita URLs, coleta links e extrai endereços de e-mail de páginas web.
2. **Email Finder**: Um script que analisa páginas web para encontrar endereços de e-mail.

Ambos os scripts podem ser executados a partir de um terminal, com suporte para a execução em diferentes ambientes.

## Requisitos

- Python 3.x
- `requests`
- `beautifulsoup4`

## Instalação

1. Clone o repositório:
`git clone <URL_DO_REPOSITORIO>`
   
2. Navegue até o diretório do projeto:
`cd <nome_do_diretorio>`

3. Certifique-se de ter o python instalado em seu sistema:

- Download: https://www.python.org/downloads/

4. Instale as bibliotecas:

- Requests: `pip install requests`
- BeautifulSoup: `pip install beautifulsoup4`

## Web Crawler

Este script visita URLs, coleta links e extrai e-mails encontrados nas páginas.

### Exemplo:

![image](https://github.com/user-attachments/assets/b82d854f-f8a4-431d-b7aa-c1dea56cc4d7)


### No PowerShell (Windows) com ativação da venv:

`.\.venv\Scripts\Activate`

`python web_crawler.py <URL>`

### No terminal (Linux) sem venv ativado:

`python3 web_crawler.py <URL>`

## Email Finder

Este script analisa uma página web para encontrar e listar endereços de e-mail.

### Exemplo:

![image](https://github.com/user-attachments/assets/a2192bfc-6021-4c9c-a8c8-5a8fb3e1d958)


### No PowerShell (Windows) com ativação da venv:

`.\.venv\Scripts\Activate`

`python email_finder.py <URL>`

### No terminal (Linux) sem venv ativado:

`python3 email_finder.py <URL>`


Substitua <URL> pela URL da página que você deseja analisar. Os scripts aceitarão URLs e processarão o conteúdo conforme especificado.
