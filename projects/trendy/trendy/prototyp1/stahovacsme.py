#from urllib.request import *
from bs4 import BeautifulSoup
import urllib.request as req

def main():
    htmltext = req.urlopen("http://bratislava.sme.sk/c/6877581/v-bratislave-sa-rodi-vela-deti-najvacsia-porodnica-nezvlada-napor.html").read()
    
    soup = BeautifulSoup(htmltext)
    
    x = soup.body.find('div', attrs={'id' : 'itext_content'}).text
    y = soup.body.find('div', attrs={'id' : 'contenth'}).find('h1').text
    print('Titulok: ' + y)
    print(x)
    
    

if __name__=='__main__':
    main()