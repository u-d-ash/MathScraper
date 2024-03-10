import requests
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

core_url = "https://kskedlaya.org/putnam-archive/"

def download_pdf(path, link):
    
    r = requests.get(link, allow_redirects=True, headers=headers)
    open(path, 'wb').write(r.content)

for i in range(1995, 2024):
    
    os.makedirs('putnam/' + str(i))
    download_pdf('putnam/' + str(i) + '/problems.pdf', core_url + str(i) + '.pdf')
    download_pdf('putnam/' + str(i) + '/solutions.pdf', core_url + str(i) + 's.pdf')