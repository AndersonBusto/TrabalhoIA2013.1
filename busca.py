import urllib2
import BeautifulSoup

request = urllib2.Request("http://www.google.com.br")
response = urllib2.urlopen(request)
soup = BeautifulSoup.BeautifulSoup(response)
for anchors in soup.findAll('a'):
    print anchors['href']
