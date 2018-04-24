import requests
from bs4 import BeautifulSoup

def get_title(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    div = soup.find_all('div',class_='listing_title')
    for d in div:
        a = d.find('a')
        print(a.text)
        with open('output/' + a.text,'w') as file:
            get_comment('https://www.tripadvisor.com.br' + a['href'],file)
            file.close()
    else:
        # Percorre a paginação
        a = soup.find('a', class_='nav next rndBtn ui_button primary taLnk')
        if a is not None: get_title('https://www.tripadvisor.com.br' + a['href'])

def get_comment(url,file):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    div = soup.find_all('div',class_='review-container')
    for d in div:
        s = d.find('span', class_='ratingDate relativeDate')
        p = d.find('p', class_='partial_entry')
        ano = int(s['title'].split('de')[2])
        # Informar o período da busca
        if ano >= 2016:
            print(p.text)
            file.write(p.text+'\n')
        else: break
    else:
        # Percorre a paginação
        a = soup.find('a', class_='nav next arrowNav taLnk')
        if a is not None: get_comment('https://www.tripadvisor.com.br' + a['href'],file)

get_title('https://www.tripadvisor.com.br/Attractions-g303518-Activities-Natal_State_of_Rio_Grande_do_Norte.html#ATTRACTION_SORT_WRAPPER')