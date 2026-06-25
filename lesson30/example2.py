from bs4 import BeautifulSoup
from fontTools.merge.util import first
from scipy.optimize import newton

from lesson30.example import html_content, paragraph_text

html_content="""
<html>
<head>
    <title>Example Page</title>
</head>
<body>
    <h1>Welcome to Beautiful soup</h1>
    <p class="intro">Beautiful soup makes web scraping easy</p>
    <div id="content">
        <p>Here are some links:</p>
        <a href="http://example.com/pages">Link 1</a>
        <a href="http://example.com/pages">Link 2</a>
        <a href="http://example.com/pages">Link 3</a>
    </div>
</body>
</html>
"""


soup = BeautifulSoup(html_content, 'html.parser')

print("Title of the page:" , soup.title.text)

intro_text = soup.find('p', class_='intro').text
print("Intro text:", intro_text)

div_content = soup.find('p', class_='intro').text
print("Intro text:", intro_text)

div_content = soup.find('div', id='content')
links = div_content.find_all('a')
for link in links:
    print("Link:", link['herf'])

first_link= soup.find('a')
print("First link text:", first_link.text)
print("Next sibling on the first link:", first_link.next_sibling)

paragraphs= soup.select('div#content p')
for paragraph in paragraphs:
    print("Paragraph insoide content", paragraph.text)

new_tag = soup.new_tag('b')
new_tag.string = "Important"
soup.h1.append(new_tag)

print("Modified h1 tag:", soup.h1)






























