import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
from tourscrape import tourscrape

html = requests.get('https://www.hmmt.org/www/archive/problems').text
soup = BeautifulSoup(html, 'lxml')

table = soup.find('div', class_ = 'justify-md-content-center text-center')

rows = table.find_all('div', class_ = 'row')

tournament_dict = {'November' : [], 'February' : []}

for row in rows[1:]:

    seetwos = row.find_all('div', class_ = 'col-2')

    for i, seto in enumerate(seetwos):

        afind = seto.find('a')
        if(afind != None):

            if(i == 0):
                tournament_dict['November'].append([afind.text.strip(), 'https://www.hmmt.org' + afind['href']])
            elif(i == 1):
                tournament_dict['February'].append([afind.text.strip(), 'https://www.hmmt.org' + afind['href']])

tourfiles = 0
 
for key in tournament_dict.keys():

    for tour in tournament_dict[key]:

        tourfiles += tourscrape('hmmt/' + key + '/' + tour[0], tour[1])

print(f"Sucessfully downloaded {tourfiles * 2} files !!!")
    
