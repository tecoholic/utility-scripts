import os
import urllib
import unicodedata

def main():
    ''' The main function to test the encoding & decoding of unicode data '''
    unifile = open('data.csv','r')
    for i,line in enumerate(unifile):
        line = line.strip("\n")
        #print type(line)
        '''s0 = unicode(line)
        s1 = s0.encode('ascii')
        s2 = urllib.unquote(s1)
        s3 = s2.decode('utf-8')
        print s3'''
        print urllib.unquote(unicode(line).encode('ascii')).decode('utf-8')
        #print line+" -> "+urllib.unquote(line)
        if i>10:
            break
        

if __name__ == "__main__":
    main()
