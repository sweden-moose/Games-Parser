from bs4 import BeautifulSoup
import requests as req

f = open('games.txt', 'r')
g = open('game-files.txt', 'w')

files = []

for i in f:
    print(i)
    resp = req.get(i.rstrip('\n'))
    soup = BeautifulSoup(resp.text, 'lxml')
    new_gamesnews = []
    last_news = []
    new_gamesnews = soup.findAll('a')
    for j in new_gamesnews:
        try:
            if str(j).index('getfile'):
                h = str(j)[str(j).index('getfile'):][:12]
                files.append(h.rstrip('\"').rstrip('\"'))
        except BaseException:
            pass

g.write('\n'.join(set(files)))
g.close()
f.close()
