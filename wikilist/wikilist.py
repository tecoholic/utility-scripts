#!/usr/bin/python

"""
http://wikistats.wmflabs.org/api.php

Wikistats API

current actions:

    -  action=dump
       -- dump csv, ssv or xml data of all tables

       option 1: format (csv|ssv|xml)
       option 2: table (wikipedias|wiktionaries|...)

       example: api.php?action=dump&table=wikipedias&format=csv
       example: api.php?action=dump&table=wikiquotes&format=ssv
       example: api.php?action=dump&table=neoseeker&format=xml
"""

import urllib2
import sys
import json
import codecs

def prepare_json(project):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'WikiList Script')]
    url = 'http://wikistats.wmflabs.org/api.php?action=dump&table={0}&format=csv'.format(project)
    print 'Opening ',url
    p = opener.open(url)
    with codecs.open('list.csv', mode='w', encoding='utf-8') as f:
        f.write(p.read().decode('utf-8'))
    # build the required data
    data = []
    with codecs.open('list.csv', mode='r', encoding='utf-8') as csvfile:
        header = csvfile.readline()
        cols= header.split(',')
        for line in csvfile.readlines():
            row = line.split(u',')
            data.append(dict(lang=row[cols.index('lang')],
                prefix=row[cols.index('prefix')],
                loclang=row[cols.index('loclang')]))
    with codecs.open(project+'.json', mode='w', encoding='utf-8') as jsonfile:
        jsonfile.write(json.dumps(data))



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python wikilist <project>\n\nSee list at http://wikistats.wmflabs.org/'
    prepare_json(sys.argv[1])
