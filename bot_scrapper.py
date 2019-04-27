import requests 
from bs4 import BeautifulSoup

def getResponse(url):
	raw_data = requests.get(url).text
	soup = BeautifulSoup(raw_data, 'html5lib')  
	content = soup.find('div', attrs = {'class':'mraOPb'})
	if content:
		return content.span.text
	else:
		content = soup.find('div', attrs = {'class':'FSP1Dd'})
		if content:
			return content.text
		else:
			return "I don't know"