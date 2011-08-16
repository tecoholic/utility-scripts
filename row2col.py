#!/usr/lib/python2.7
'''
Python Script to convert the rows to columns of a CSV file
'''
import sys

def row2col(filename):
    ''' Function which converts rows to colmns '''
    csvFile = open(filename, "r")
    fileLines = csvFile.readlines()
    csvFile.close()

    #newCSVfile = open(filename, "w")
    
    newFileLines = []
    for line in fileLines[0].split(","):
        newline = [line.strip("\n")]
        newFileLines.append(newline)

    for i,line in enumerate(fileLines):
        if i > 0:
            row = line.split(",")
            for j,celldata in enumerate(row):
                newFileLines[j].append(celldata.strip("\n"))

    newFile = open(filename, "w")
    for line in newFileLines:
        newFile.write(",".join(word for word in line))
        newFile.write("\n")
    newFile.close()



if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        row2col(filename)
    else:
        print "Error: Inavlind number of perameters.\nUsage: python row2col.py file.csv"

