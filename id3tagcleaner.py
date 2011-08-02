#!/usr/bin/python
'''
TAG CLEANER
------------

It is Python script which when run will take a base directory as input and search for all the mp3 
files in the directory and remove wesite addresses from the ID3 tag values automatically.

Dependencies:
-------------

It uses the Mutagen ID3 library for parsing ID3 tag values from files and for modifying them.
Make sure you have Mutagen installed before attempting to run this script.

1. Mutagen Python Library:
    You can find about Mutagen Library at http://code.google.com/p/mutagen/

'''

import re
import string
import sys
import os
import time
from datetime import date
from mutagen.mp3 import  MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3


def listFilePath(directory):
    """ Funtion to list the files in a directory.\n
    It takes one value as input: \n\tA string specifying the root directory.\n
    It returns one list:\n\tList of path of all files in the given directory and its sub-directories\n"""
    fileList=[]
    #preparing list of directories
    try:
        dirList = [d for d in os.listdir(directory)
                   if os.path.isdir(os.path.join(directory,d))]
        #preparing list of files
        for f in os.listdir(directory):
            if os.path.isfile(os.path.join(directory,f)):
                              name,ext = os.path.splitext(f)
                              if str(ext).lower()==".mp3":
                                  fileList.append(os.path.join(directory,f))
        if len(dirList) == 0:
            return fileList #return list of files if there are no sub-directories
        else:   #otherwise recurse into sub-directories and retrive filenames
            for di in dirList:
                crntDir = os.path.join(directory,di)
                fileList.extend(listFilePath(crntDir))
            return fileList
    except OSError:
        print 'Inavlid Directory!! Please check the diretory you entered.'


def remove_site(tag):
    """ The function takes a string and removes website address"""
    p=re.compile('(http://)?w{0,3}\.?\w+\.[a-z]{2,3}(\.[a-z]{2,3})?',re.IGNORECASE) #RE expression for the web address. Feel free to edit 
    comParts = string.split(tag)#split the string at spaces
    try:
        if len(comParts)>0:     #to make sure the value is not empty
            for i in range(len(comParts)):
                '''Using the RE to find wether the string contains a web address'''
                comParts[i]=string.strip(comParts[i]) #Strip and white extra white spaces before or after
                if p.search(comParts[i]):
                    comParts.pop(i)
                if len(comParts[i])==1:
                    comParts.pop(i)
                if (comParts[i]=='Riya')|(comParts[i]=='collections'):
                    comParts.pop(i)
                         
    except IndexError:
        newTag=''
    newTag = " ".join("%s" %comParts[k] for k in range(len(comParts)))
    if newTag=='':
        newTag='unknown'
    return newTag

    

direc = raw_input('Enter the root directory or path:')

files = listFilePath(direc)

try:
    #Create the log file
    nfile = open(os.path.join(direc,"mp3.log"),'w')
    nfile.write(str(date.today())+'\n')
    nfile.write(str(time.asctime())+'\n')
    nfile.write('\nInput Directory:'+direc)
    nfile.write('\nFiles Processed\n----------------\n\n')
    nfile.close()
except IOError:
    print 'Unable to create log file.'

try:
    #Open the log file to append data
    afile = open(os.path.join(direc,"mp3.log"),'a')
except IOError:
    print 'Unable to add data to log file.'

for i in range(len(files)):    
    afile.write(str(i)+':'+files[i]+' --> ')
    try:
        audio = MP3(files[i],ID3=EasyID3)
        if len(audio.keys()) > 0:
            for k in audio.keys():
                audio[k] = remove_site(audio[k][0])
                audio.save()
        afile.write('Processed\n')
    except IOError:
        afile.write('Cannot Process. IO Error.\n')
afile.close()
print 'tagEditor has finished....If you still see website addresses in your mp3 files. Try rerunning the script again few times.. on any error contact arunmozhi@ieee.org with the error'
