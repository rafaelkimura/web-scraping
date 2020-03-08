from bs4 import BeautifulSoup as bs
import requests
import os
import wget

linkpath = 'http://pet.inf.ufpr.br/farol/repositorio/provas/'
savepath = './'

def downfiles(linkpath, savepath):
	page = requests.get(linkpath)
	soup = bs(page.content, 'html.parser')
	lista = soup.find_all('tr')[3:]
	
	for elem in lista:
		if(str(elem).find("colspan") == -1):			
			td = elem.findChildren("td")
			isfolder = str(td[-2]).split(">")[1].split("<")[0].replace(" ","")
			if isfolder == '-':
				foldername = (str(elem.findChildren("a")).split(">")[1].split("<")[0])
				newsavepath = savepath + foldername	
				os.mkdir(newsavepath)
				downfiles(linkpath + foldername, newsavepath)
			else:
				filename = (str(elem.findChildren("a")).split(">")[1].split("<")[0])
				wget.download(linkpath + filename, out=savepath)
				

downfiles(linkpath, savepath)			









