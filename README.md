# A-Guide-to-Django
Crawl of Vitor Freitas's "[A Complete Beginner's Guide to Django](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/)"

## Setup

1. Packages

```
pip install requests
pip install beautifulsoup4
pip install pdfkit
```

2. [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

```
Win:
	Download and add to $PATH
Linux:
	apt-get install wkhtmltopdf
or   yum intsall wkhtmltopdf
```

## Usage

1. Set the path of wkhtmltopdf in crawl.py (line 6);

2. Set the font size in crawl.py (line 56);

## Improvements Needed

1. Superfluous `, '\n',`
2. Typesetting

## Acknowledge

[Vitor Freitas](https://simpleisbetterthancomplex.com/)