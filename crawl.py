# -*- coding=utf-8 -*-
import os
import pdfkit
import requests
from bs4 import BeautifulSoup
config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    {head}
</head>
<body>
{content}
</body>
</html>
"""

def parse_url_to_html(url, name):

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        head = soup.find_all("h3", "post-title")
        body_tag = soup.article
        body = body_tag.contents

        html = html_template.format(content=body,head=head)
        html = html.encode("utf-8")
        with open(name, 'wb') as f:
            f.write(html)
        return name

    except Exception as e:
        print(e)

def save_pdf(htmls, file_name):

    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
        'minimum-font-size': 40,
    }

    pdfkit.from_file(htmls, file_name, options=options,configuration=config)

head = 'https://simpleisbetterthancomplex.com/'
url  = 'https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/'
urls = []

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
series = soup.find(class_="series")

for a in series.ul.find_all("a"):
    href = str(a.get('href'))
    result = href.find('/')
    url = head + href
    urls.append(url)

htmls = [parse_url_to_html(url, str(index) + ".html") for index, url in enumerate(urls)]
print(htmls)

file_name = 'A Complete Beginner\'s Guide to Django.pdf'
save_pdf(htmls, file_name)

for html in htmls:
    os.remove(html)