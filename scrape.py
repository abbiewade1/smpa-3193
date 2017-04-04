import csv
import requests
from BeautifulSoup import BeautifulSoup
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

months = ['04', '03', '02', '01']
list_of_rows = []

for month in months:
	print month
	response = requests.get("http://m.nationals.mlb.com/roster/transactions/2017/" + month)
	html = response.content

	soup = BeautifulSoup(html)
	table = soup.find('table')

	for row in table.findAll('tr'):
    		list_of_cells = []
    	for cell in row.findAll('td'):
    		list_of_cells.append(cell.text.encode('utf-8'))
    	list_of_rows.append(list_of_cells)
    	
	soup = BeautifulSoup(html)
	links = soup.find_all('a')

	for tag in links:
		link = tag.get('href', None)
		if link is not None:
			print link

outfile = open("transactions.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["date", "url", "text"])
writer.writerow(list_of_rows)