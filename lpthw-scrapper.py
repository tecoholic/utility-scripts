import urllib2
import os
import sys

from BeautifulSoup import BeautifulSoup as bs

# Meta Variables
__filename__ = "lpthw-scrapper.py"
__version__ = 0.1
__desc__ = "A scrapper program to automatically download the html pages of\
        Learn Python The Hard Way"
__author__ = "tecoholic"

#Program Variables
url = "http://learnpythonthehardway.org/book/"
location = "/home/teco/Documents/"

def create_folder(path):
    '''Function creates required folders to put contents'''
    newdir  = os.path.join(path, "lpthw")
    if not os.path.isdir(newdir):
        os.makedirs(newdir)
        print "Created new directory:"+newdir
    if not os.path.isdir(os.path.join(newdir, "_static")):
        os.makedirs(os.path.join(newdir, "_static"))
        print "Created new directory:"+os.path.join(newdir, "_static")
    return newdir

def process_html(html):
    '''Fucntion gets html string, makes a soup, prcesses and returns string'''
    soup = bs(html)
    scripts = soup.findAll("script")
    [script.extract() for script in scripts]
    return str(soup)

def download():
    '''Fuction to download the pages'''
    folder = create_folder(location)
    cssfolder = os.path.join(folder, "_static")
    opener = urllib2.build_opener()
    opener.addheaders = [("User-agent" , "Mozilla/5.0")]
    
    # index.html
    link = opener.open(url)
    homepage = link.read()
    indexfile = open(os.path.join(folder, "index.html"), "w")
    indexfile.write(process_html(homepage))
    indexfile.close()
    opener.close()
    
    # other files
    soup = bs(homepage)
    pagelis = soup.findAll("li", {"class" : "toctree-l1"})
    for li in pagelis:
        newlink = opener.open(url+li.a["href"])
        newfile = open(os.path.join(folder,li.a["href"]), "w")
        newfile.write(process_html(newlink.read()))
        newfile.close()
        newlink.close()
    
    # add some css
    css = soup.findAll("link", { "type" : "text/css" })
    for cs in css:
        cslink = opener.open(url+cs["href"])
        path,fil = os.path.split(url+cs["href"])
        csfile = open(os.path.join(cssfolder, fil), "w")
        csfile.write(cslink.read())
        csfile.close()
        cslink.close()
    
    # extra code to satisfy @import in the css. Aaaaarrrrgh
    cslink = opener.open(url+"_static/basic.css")
    csfile = open(os.path.join(cssfolder, "basic.css"), "w")
    csfile.write(cslink.read())
    csfile.close()
    cslink.close()


if __name__ == '__main__':
    download()
