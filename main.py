from bs4 import BeautifulSoup
import requests

url = requests.get('https://quotes.toscrape.com/').text
soup = BeautifulSoup(url, 'lxml')

content = soup.find('div', class_ = 'container')

#extracting the main heading
heading = content.find('div', class_ = 'col-md-8')
print(heading.text)

#extracting the quotes of a webpage
quotes = content.find()

