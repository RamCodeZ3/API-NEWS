import requests
from bs4 import BeautifulSoup

URL = 'https://www.diariolibre.com/ultima-hora'
answer = requests.get(URL)

soup = BeautifulSoup(answer.text, 'html.parser')
notice = soup.find_all("div", class_="w-full sm:w-9/12 sm:pl-2")

for n in notice:
    print(n)


if __name__ == '__main__':
    pass