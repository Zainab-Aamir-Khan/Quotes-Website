from bs4 import BeautifulSoup
import requests

url = requests.get('https://quotes.toscrape.com/').text
soup = BeautifulSoup(url, 'lxml')

main = soup.find('div', class_ = 'container')

 #extracting the main heading
heading = main.find('div', class_ = 'col-md-8').text.strip()
print(heading)

for quote in main.find_all('div', class_ = 'quote'):


    #extracting the quotes of a webpage
    quotes = quote.find('span', class_ = 'text').text
    print(quotes)

    writer = quote.find('small', class_ = 'author').text
    print(writer)

    tags = quote.find('a',class_ = 'tag').text
    print(tags)
    


