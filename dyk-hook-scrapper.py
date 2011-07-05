'''
This File scraps the DYK hooks and stores the data in CSV files.
'''
import os
import urllib
import codecs

import BeautifulSoup

directory = "hookhtmls"

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
        lis  = soup.findAll("li",
                            attrs={"style":"-moz-float-edge: content-box"})
        for index, li in enumerate(lis):
            try:
                link = li.b.a["href"]
            except TypeError:
                link = li.find("a")["href"]
            link = link.replace("/wiki/","")
            #title = urllib.unquote(link)
            content = unicode(li).replace(",",";")
            csvfile.write(fil.replace(".html","-")+str(index)+","+link+","+content+"\n")
            print link
    csvfile.close()
            #break
        #break
    
    
if __name__ == "__main__":
    main()
