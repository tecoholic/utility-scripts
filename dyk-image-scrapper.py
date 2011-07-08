''' This file scrapes the images from the DYK archives and associates the images
with the respective hooks '''
import os
import urllib
import codecs

import BeautifulSoup

directory = "hookhtmls"

def analyser():
    files = os.listdir(directory)
    for fil in files:
        print fil
        html = open(os.path.join(directory,fil), "r")
        soup = BeautifulSoup.BeautifulSoup(html.read())
        #h3 = soup.find('h3')
        div = soup.findAll('div',
                          attrs={'style':'float:right;margin-left:0.5em;'})
        print 'With Semicolon:',len(div)
        imagecount = 0
        for di in div:
            try:
                img = di.find('img')
                if img != None:
                    imagecount += 1
            except:
                pass
        print 'Images:',imagecount
        imagecount = 0
        div = soup.findAll('div',
                          attrs={'style':'float:right;margin-left:0.5em'})
        print 'Without Semicolon:',len(div)
        for di in div:
            try:
                img = di.find('img')
                if img != None:
                    imagecount += 1
            except:
                pass
        print 'Images:',imagecount
        
        
        

def scraper(selector):
    '''this function scrapes the image data and writes it to the csv file'''
    sno = 1
    files = os.listdir(directory)
    imagefile = codecs.open("images.csv", encoding='utf-8', mode='w+')
    imagefile.write("sno,title,imgtitle,src,alt\n")
    for fil in files:
        print fil        
        html = open(os.path.join(directory,fil), "r")
        soup = BeautifulSoup.BeautifulSoup(html.read())
        h3 = soup.find('h3')
        div = h3.findNext('div',
                          attrs={'style' : selector})
        #print div
        while div != None:    
            li = div.findNext("li",
                              attrs={'style':'-moz-float-edge: content-box'})
            try:
                link = li.b.a['href']
            except TypeError:
                link = li.find("a")["href"]
            link = link.replace("/wiki/","")
            title = urllib.unquote(unicode(link).encode('ascii')).decode('utf-8')
            title = " ".join(title.split('_')).replace(",",";")
            print title
            try:
                imgAnchor = div.find("a", attrs={'class':'image'})
                imgtitle = unicode(imgAnchor["title"]).replace(",",";")
                img = imgAnchor.find("img")
                src = unicode(img['src']).replace(",",";")
                alt = unicode(img['alt']).replace(",",";")
                
                imagefile.write(str(sno)+","+title+","+imgtitle+","+src+","+alt+"\n")
                sno += 1
            except:
                print "Image Unavailable"
            div = div.findNext('div',
                               attrs={'style':'float:right;margin-left:0.5em;'})
            #print "nextdiv",div.a["title"]
    imagefile.close()
                
                
def main():
    ''' the main function to do the scrapping '''
    selectors=['float:right;margin-left:0.5em;','float:right;margin-left:0.5em']
    for select in selectors:
        scraper(select)

        
if __name__ == "__main__":
    #main()
    analyser()
