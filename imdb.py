import requests
from bs4 import BeautifulSoup

try:
    url = requests.get('https://www.imdb.com/chart/top/')
    url.raise_for_status()

    soup=BeautifulSoup(url.text,'html.parser')

    movies = soup.find('tbody', class_="lister-list").find_all('tr')
    for movie in movies:
        name = movie.find('td' , class_="titleColumn").a.text
        rank = movie.find('td' , class_="titleColumn").get_text(strip=True).split('.')
        year = movie.find('td' , class_="titleColumn").span.text.strip('()')
        rating = movie.find('td' , class_="ratingColumn imdbRating").strong.text
        print(name,rank,year,rating)

except Exception as e:
    print(e)