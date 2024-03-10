import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path

def download_pdf(path, link):
    
    r = requests.get(link, allow_redirects=True)
    open(path, 'wb').write(r.content)

def tourscrape(tourname, link):

    html = requests.get(link).text
    soup = BeautifulSoup(html, 'lxml')

    table = soup.find('table', class_ = 'display-tournament')
    trs = table.find_all('tr')

    tournament_matrix = []

    for tr in trs:

        section = []

        tdx = tr.find_all('td')
        
        for i, td in enumerate(tdx):

            if(i == 0):
                secname = td.text
                secname = secname.rstrip()
                section.append(secname)
            else:
                section.append('https:' + td.find('a')['href'])
        
        tournament_matrix.append(section)

    #print(tournament_matrix)

    for sect in tournament_matrix[:-1]:

        os.makedirs(tourname + '/' + sect[0])

        download_pdf(tourname + '/' + sect[0] + '/problems.pdf', sect[1])
        download_pdf(tourname + '/' + sect[0] + '/solutions.pdf', sect[2])
    

    return len(tournament_matrix)

