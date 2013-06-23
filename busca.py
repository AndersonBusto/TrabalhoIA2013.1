import urllib2
import BeautifulSoup

links = []
limite = 1

def buscaProfundidadeIterativa(url1, url2):

    global limite

    if url1 == url2:
        return 

    if limite == 1
	return

    requisicao = urllib2.Request(url1)
    resposta = urllib2.urlopen(requisicao)
    soup = BeautifulSoup.BeautifulSoup(resposta)
    for anchors in soup.findAll('a'):
        links << anchors['href']


