from enum import IntEnum
from geopy.geocoders import Nominatim

class DoctorIdx (IntEnum):
    TITLE = 0
    FIRST = 1
    LAST = 2
    DEGREE = 3
    ADDRESS = 4
    CITY = 5
    COUNTY = 6
    STATE = 7
    ZIPCODE = 8
    PHONE = 9
    FAX = 10

geolocator = None

def processAddress(row, loc):
    if fieldsAreMissingFrom(row):
        return ""

    fullAddress = buildAddress(row)
    point = getLatLonFromAddress(fullAddress)
    
    # only output 
    #dbugLog(["Search Address", fullAddress], point)

    return point


def fieldsAreMissingFrom(row):
    return len(row) < 10


def buildAddress(row):
    address = row[DoctorIdx.ADDRESS]
    city = row[DoctorIdx.CITY]
    state = row[DoctorIdx.STATE]

    if (not address or not city or not state):
        return ""

    fullAddress = address + ' ' + city + ', ' + state
    return fullAddress

geolocator = None
def getLatLonFromAddress(address):
    try:
        geolocator
    except NameError:
        geolocator = Nominatim(user_agent="samsa-map")

    location = geolocator.geocode(address)

    if not isValid(location):
        invalidLocation = {
            'latitude': 1.0,
            'longitude': 1.0
        }
        return invalidLocation
    
    return location

def isEmpty(point):
    try:
        return point is not None or not point.latitude or not point.longitude
    except AttributeError:
        return True

def isValid(point):
    valid = True
    try: 
        point
    except AttributeError:
        valid = False
    
    try: 
        point.latitude
    except AttributeError:
        valid = False

    try: 
        point.longitude
    except AttributeError:
        valid = False
    
    return valid

def dbugLog(args, point):
    debugTitle = args[0].upper()
    print("*** START %s DEBUG LOG ***" % debugTitle)
    for i in range(1, len(args)):
        print("\t" + args[i])
    print("***  END %s DEBUG LOG  ***\n" % debugTitle)

    if (isValid(point)):
        print("\t-->" + str(point.latitude) + " " + str(point.longitude))
    else: 
        print("\tNo point extracted")

