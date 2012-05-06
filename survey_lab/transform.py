'''
Program to perform rotation and translation to a set of co-ordinates w.r.t a point
'''
import math
import sys
import csv

input_file = "coords.csv"
output_file = "newcoords.csv"

xorg = 1000
yorg = 1000

angle = -math.atan(47.083/46.128)

# The functions that perform the required rotation and translation
def translateX( x, y ):
  return xorg + ((x - xorg) * math.cos(angle)) - ((y - yorg) * math.sin(angle))

def translateY( x, y ):
  return yorg + ((yorg - y) * math.cos(angle)) - ((x - xorg) * math.sin(angle))

def main():
  reader = csv.DictReader(open(input_file, 'rb'))
  writer = csv.DictWriter(open(output_file,'wb'), ['STATION','NORTH','EAST','SNO','TYPE'])
  writer.writeheader()
  for row in reader:
    newX = translateX(float(row['EAST']), float(row['NORTH']))
    newY = translateY(float(row['EAST']), float(row['NORTH']))
    row['EAST'] = "%.3f" % newX
    row['NORTH'] = "%.3f" % newY
    writer.writerow(row)

if __name__ == '__main__':
  if len(sys.argv)> 2:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    print translateX(x,y),translateY(x,y)
  elif len(sys.argv) == 1:
    main()
  else:
    print "Usage: python transform.py [Easting] [Northing]"
