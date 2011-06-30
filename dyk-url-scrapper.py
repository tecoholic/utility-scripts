''' This file gets the archive page urls from the DYK Recent Additions page'''
import urllib2

import BeautifulSoup

base_url = "http://en.wikipedia.org/wiki/Wikipedia:Recent_additions"

def main():
    ''' test main '''
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    f = opener.open(base_url)
    soup = BeautifulSoup.BeautifulSoup(f.read())
    table = soup.find("table",attrs={"style":"background:none; width:700px"})
    cells = table.findAll("td")
    result = open("urls.log","w+")
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
        
if __name__ == "__main__":
    main()
