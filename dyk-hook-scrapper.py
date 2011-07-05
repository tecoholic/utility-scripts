'''
This File scraps the DYK hooks and stores the data in CSV files.
'''
import os
import urllib
import codecs

import BeautifulSoup

directory = "hookhtmls"


def newMain():
    ''' new Scrapper that would scarp image data along with it '''
    hookfile = codecs.open("hook.csv", mode="w+", encoding='utf-8')
    hookfile.write("sno,identifier,title,link,text\n")
    sno = 1
    files = os.listdir(directory)
    for fil in files:
        print fil
        html = open(os.path.join(directory,fil), 'r')
        soup = BeautifulSoup.BeautifulSoup(html.read())
        hooklis  = soup.findAll("li",
                            attrs={"style":"-moz-float-edge: content-box"})
        for index,hook in enumerate(hooklis):
            try:
                link = hook.b.a["href"]
            except TypeError:
                link = hook.find("a")["href"]
            link = link.replace("/wiki/","").replace(",",";")
            title = urllib.unquote(unicode(link).encode('ascii')).decode('utf-8')
            title = " ".join(title.split('_')).replace(",",";")
            content = unicode(hook).replace(",",";")
            iden = fil.replace(".html","-")+str(index)
            hookfile.write(str(sno)+","+iden+","+title+","+link+","+content+"\n")
            print sno,title
            sno += 1
    hookfile.close()
    
if __name__ == "__main__":
    newMain()
