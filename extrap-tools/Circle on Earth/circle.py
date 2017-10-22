from math import cos
from math import sin
from math import pi
from math import radians

#prints out area of search in km^2 and mi^2
def report(r):
    areakm = pi * r ** (2)
    areami = areakm * 0.386102
    print('Area (square km) : ' + str(areakm))
    print('Area (square mi) : ' + str(areami))

#takes in latitude, longitude, and radius, and creates a circle on the earth
#take these coordinates and put them in a KML file.
def create_circle(flat,flong,r):
    f = open(r'circlecoord.kml', 'a')
    f.write('<coordinates>' + '\n')
    for n in range(361):
        nlat = flat + ((r * cos(radians(n))) / 110.574)
        nlong = flong + ((r * sin(radians(n))) / (111.320 * cos(radians(nlat))))
        f.write(str(nlong) + ',' + str(nlat) + ',1100' + '\n')
    f.write('</coordinates>')
    f.close()
    report(r)
