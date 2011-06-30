''' This file gets the archive page urls from the DYK Recent Additions page'''
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
    logfile = open("urls.txt", "r")
    
    for i in range(count):
        line = logfile.readline()
        if i >= skip:            
            url = "http://en.wikipedia.org" + line.replace("\n","")
            line = line.replace("/wiki/Wikipedia:Recent_additions/","").replace("\n","")
            line = line.replace("/","-")+".html"
            print line
            opener = urllib2.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            f = opener.open(url)
            print f.info()
            print "Downloading...."
            soup = BeautifulSoup.BeautifulSoup(f.read())
            html = open(line,"w+")
            html.write(str(soup))
            html.close()
            print line + " -> Finished"
            f.close()
        
        
def main():
    # Uncomment the below line to get the urls of all archive pages
    #get_urls()
    #Uncomment the following line to download the html responses and
    #save them as html files. Parameters(index,skip) 
    #Note: skip skips first "skip" no.of files
    #download_html(5,4)
        
if __name__ == "__main__":
    main()
