from math import cos
from math import sin
from math import radians

#calculates the change in northward position given velociy, bearing, and time
def dN(v,b,t):
    dN = (v * cos(radians(b)) * t) / 1000
    return dN

#calculates a change in latitude given a change in y (northward)
def dlat(xn):
    dlat = xn / 110.574
    return dlat

#calculates a change in x (eastward) position based off velocity, bearing, and time
def dE(v,b,t):
    dE = (v * sin(radians(b)) * t) / 1000
    return dE

#calculates change in longitude given a change in x (eastward)
def dlon(xe,lat):
    dlon = xe / (111.320 * cos(radians(lat)))
    return dlon

#extrapolates next position given an initial geographical position,
#velocity, bearing, and time in that velocity
def extrap(lat0,lon0,v,b,t):
    Nc = dN(v,b,t)
    latc = dlat(Nc)
    lat = lat0 + latc
    
    Ec = dE(v,b,t)
    lonc = dlon(Ec,lat)
    lon = lon0 + lonc
    return [lat,lon]

#draws an arc on the earth given a range of velocities, bearings, an initial position
#and time
def extraparc(lat0,lon0,v1,v2,b1,b2,t):
    f = open('arc.kml', 'a')
    f.write('<coordinates>\n')
    #range 101 calculates all positions for the a given weight of v1 and v2
    for n in range(101):
        v = (n/100) * v1 + ((100-n) / 100) * v2
        b = (n/100) * b1 + ((100-n) / 100) * b2
        coords = extrap(lat0,lon0,v,b,t)
        f.write(str(coords[1]) + ',' + str(coords[0]) + ',0\n')
    f.write('</coordinates>')
    f.close()


        
    
