''' This file gets the archive page urls from the DYK Recent Additions page'''
import os
import urllib2

import BeautifulSoup

base_url = "http://en.wikipedia.org/wiki/Wikipedia:Recent_additions"

def get_urls():
    ''' This function scrapes all archive url and stores in urls.log'''
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    f = opener.open(base_url)
    soup = BeautifulSoup.BeautifulSoup(f.read())
    table = soup.find("table",attrs={"style":"background:none; width:700px"})
    cells = table.findAll("td")
    result = open("urls.txt","w+")
    for cell in cells:
        print cell
        link = cell.find("a")
        try:
            result.write(link["href"])
            result.write("\n")
        except TypeError:
            pass
    result.close()
    f.close()
    
def download_html(count,skip):
    ''' This function dowloads the htmlpages of given count '''
    print os.listdir(".")
    logfile = open("urls.txt", "r")
    
    for i in range(count):
        if i < skip:
            continue
        line = logfile.readline()
        url = "http://en.wikipedia.org" + line.replace("\n","")
        line = line.replace("/wiki/Wikipedia:Recent_additions/","").replace("\n","")
        line = line.replace("/","-")+".html"
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        f = opener.open(url)
        soup = BeautifulSoup.BeautifulSoup(f.read())
        html = open(line,"w+")
        html.write(str(soup))
        html.close()
        print line
        f.close()
        
        
        
def main():
    #get_urls()
    download_html(1,0)
        
if __name__ == "__main__":
    main()
