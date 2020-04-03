import csv
import enum
from geopy.geocoders import Nominatim

class DoctorField (enum.Enum):
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


geolocator = Nominatim(user_agent="samsa-map")
# location = geolocator.geocode("175 5th avenue nyc")
# print 

with open('t.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    rowCount = 0
    for row in data:
        if (len(row) < 10):
            continue
        rowCount = rowCount + 1
        print("row %s"% rowCount)
        address = row[DoctorField.ADDRESS]
        city = row[DoctorField.CITY]
        state = row[DoctorField.STATE]
        addrToSearch = address + ', ' + city + ', ' + state
        if (address and city and state):
            print(addrToSearch)
            location = geolocator.geocode(addrToSearch)
            if (location is None): continue
            else: print("location not found")
            if (location.latitude and location.longitude):
                print(location.latitude, location.longitude)
            else: 
                print("unable to find lat/lon")
        else: 
            print ("No address in this row")

        #for item in row:
        #for idx, item in enumerate(row):
        #    print(item)
        #print(', '.join(row))
