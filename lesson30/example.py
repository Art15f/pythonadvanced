from bs4 import BeautifulSoup
from markdown_it.rules_block import paragraph

html_content = "<html><body><p>Hello, Beautiful Soup!</p></body></html>"

soup = BeautifulSoup(html_content, 'html.parser')

paragraph_text = soup.find('p').text

print(paragraph_text)