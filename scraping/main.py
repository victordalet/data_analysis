import requests,time
from bs4 import BeautifulSoup

def main(url_base):
	links = []

	response = requests.get(url)

	for i in range(26):
		url = url_base+'/places/default/index/'+str(i)
		response = requests.get(url)
		print(response)
		if response.ok:
			print('Page : '+str(i))
			soup = BeautifulSoup(response.text,'lxlm')
			tds = soup.findAll('td')
			for td in tds :
				a = td.find('a')
				links = a['href']
				links.append(url_base+links)
			time.sleep(3)

	print(len(links))

	with open('urls.txt','w') as file:
		for link in links:
			file.write(links+'\n'
				)
main('http://example.webscraping.com/')