import csv
import requests
from BeautifulSoup import BeautifulSoup

batch_size = 2
urllist = ["https://columbian.gwu.edu/2010-2011", "https://columbian.gwu.edu/2015-2016"]
url_chunks = [urllist[x:x+2] for x in xrange(0, len(urllist), batch_size)]

def scrape_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    h1 = soup.find("h1", class_= "class-headline")
    return (h1.get_text())

def scrape_batch(url_chunk):
    chunk_resp = []
    for url in url_chunk:
        chunk_resp.append(scrape_url(url))
    return chunk_resp

for url_chunk in url_chunks:
    print scrape_batch(url_chunk)

list_of_rows = []
for row in table.findAll('tr')[1:-1]:
    list_of_cells = []
    for cell in row.findAll('td'):
    	list_of_cells.append(cell.text)
    list_of_rows.append(list_of_cells)

outfile = open("college.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["department", "faculty", "sponsor", "title", "year"])
writer.writerow(list_of_rows)
