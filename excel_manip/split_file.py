'''
This file splits the 3 row census data in TN.csv into 3 different files of 1 row each.
'''

import sys

def main(filename):
    ''' The main function '''
    f = open(filename, 'r')
    r1 = open("total.csv", 'w')
    r2 = open("urban.csv", 'w')
    r3 = open("rural.csv", 'w')
    col = f.readline()
    r1.write(col)
    r2.write(col)
    r3.write(col)
    for line in f:
        if 'Total' in line:
            r1.write(line)
        elif 'Urban' in line:
            r2.write(line)
        elif 'Rural' in line:
            r3.write(line)
    f.close()
    r1.close()
    r2.close()
    r3.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print 'Error: Input file not given.\nUsage: python split_file.py TN.csv'

