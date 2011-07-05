import os
import urllib
import codecs

import BeautifulSoup

directory = "hookhtmls"

def extract_data(div, ul):
    ''' This Function extracts the data from the div and the ul '''

    imagefile = codecs.open("image.csv", encoding='utf-8', mode='w+')
    
    lis = ul.findAll('li',
                     attrs={ 'style': '-moz-float-edge: content-box'} )
    for index, li in enumerate(lis):
        try:
            link = li.b.a["href"]
        except TypeError:
            link = li.find("a")["href"]
        link = link.replace("/wiki/","")
        title = urllib.unquote(unicode(link).encode('ascii')).decode('utf-8')
        title = " ".join(title.split('_'))
        #print title
        
        if index == 0:
            image = div.find('img')
            image_data = { 'alt' : image["alt"],
                           'src' : image["src"] }
    

def main():
    ''' test main '''
    files = os.listdir(directory)
    csvfile = codecs.open("data.csv", encoding='utf-8', mode='w+')
    csvfile.write("id,link,text\n")
    for fil in files:
        print fil
        #csvfile = codecs.open(str(fil).replace("html","csv"), encoding='utf-8', mode='w+')
        html = open(os.path.join(directory,fil), "r")
        soup = BeautifulSoup.BeautifulSoup(html.read())
        h3 = soup.find('h3')
        firstDiv = h3.findNext('div',
                               attrs={'style':'float:right;margin-left:0.5em;'})
        #print unicode(firstDiv.p.a.img["alt"])
        while firstDiv != None:
            ul = firstDiv.findNext("ul")
            extract_data(firstDiv, ul)
            firstDiv = ul.findNext('div',
                                   attrs={'style':'float:right;margin-left:0.5em;'})
            break
        break

if __name__ == "__main__":
    main()
