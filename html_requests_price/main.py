import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re
import pprint


def get_session():
    s = requests.Session()
    return s


def get_links(s, url):
    r = s.get(url, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = [link.attrs['href'] for link in soup.find_all('a')]
    pprint(links)
    return links


def get_links_session(s, url):
    r = s.get(url, verify=False)
    r.html.render(sleep=3)
    # salva o html da página que foi renderizada
    # with open('result.html', 'w+') as f:
    #    f.write(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    product = soup.find_all('template', {'data-varname': '__STATE__'})
    # salva o json dos dados coletados pela pagina
    with open('produc.json', 'w') as f:
        json.dump(f, indent=4)
    print('Dados salvo.')
    # return links


if __name__ == '__main__':
    url = 'https://seminovos.localiza.com/argo?map=ft&order=OrderByPriceASC'
    # links = get_links(get_session(), url)
    s = HTMLSession()
    links = get_links_session(s, url)
    for link in links:
        print(link)
