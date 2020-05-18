from bs4 import BeautifulSoup
import requests as req

f = open('games.txt', 'w')
games = []
max_page = 0

resp = req.get("https://freetp.org")
soup = BeautifulSoup(resp.text, 'lxml')
gamesnews = soup.findAll('div', class_='mainside')
for i in range(len(gamesnews)):
    if gamesnews[i].find('div', class_='heading') is not None:
        new_gamesnews = gamesnews[i].findAll('a')
for i in new_gamesnews:
    if i.get('href')[:24] == 'https://freetp.org/page/':
        if max_page < int(i.get('href')[24:-1]):
            max_page = int(i.get('href')[24:-1])

for i in range(1, max_page + 1):
    print(f"Current page : {i}")
    resp = req.get(f"https://freetp.org/page/{i}/")
    soup = BeautifulSoup(resp.text, 'lxml')
    new_gamesnews = []
    gamesnews = soup.findAll('div', class_='mainside')
    for i in range(len(gamesnews)):
        if gamesnews[i].find('div', class_='heading') is not None:
            new_gamesnews = gamesnews[i].findAll('a')
    for i in new_gamesnews:
        if i.get('href')[:27] == 'https://freetp.org/po-seti/':
            games.append(i.get('href').rstrip('#comment'))
print(*set(games), sep='\n')
f.write('\n'.join(set(games)))
f.close()
