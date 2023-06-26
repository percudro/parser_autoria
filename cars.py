from queue import Empty
import requests
from bs4 import BeautifulSoup
import csv


url = 'https://auto.ria.com/uk/newauto/search/'
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept" : "*/*"
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
cars = []
items = soup.find_all('section', class_='proposition')

def power(s):
    pow = list()
    for i in range(len(s)-2):
        try:
            pow.append(int(s[i:i+3]))
        except:
            continue
        try:
            return max(pow)
        except:
            return 0

k=1 
while k!=332:
        next_page_relative_url = '?page={}&'.format(k)
        r = requests.get(url + next_page_relative_url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        items = soup.find_all('section', class_='proposition')
        for item in items:
            cars.append({
            'title' : item.find('h3', class_='proposition_name').text.strip(),
            'price_d': item.find('div', class_='proposition_price').text.split("$")[0].replace(' ', ''),
            'horse_powers': power(item.find('div', class_='proposition_equip size13').text.strip())
            })
        csv_file = open('cars.csv', 'a', encoding='utf-8', newline='')
        writer = csv.writer(csv_file)
        for car in cars:
            writer.writerow(car.values())
        csv_file.close()    
        print(str(k) + " -> " + str(k/332*100)+"%")
        k+=1
        cars.clear()