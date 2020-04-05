#!/usr/local/bin/python3

import csv
import csv_converter as converter

def convertPointsIteratively():
    file = 'sample-data.csv'
    data = getDataFromCSV(file)
    dataProcessor = converter.processAddress
    points = convertToPoints(data, dataProcessor)
    for point in points:
        print("checking point....")
        try:
            print("\tpoint @ % s, % s"% (str(point.latitude), str(point.longitude)))
        except AttributeError: 
            print("\tno valid point")

def getDataFromCSV(file):
    data = []
    with open(file) as csvfile:
        dataItr = csv.reader(csvfile, delimiter=',', quotechar='|')
        count = 0
        for row in dataItr:
            data.append(row)
    return data
        
def convertToPoints(data, callback):
    count = 0
    results = []
    for row in data:
        count = count + 1
        point = callback(row, count)
        results.append(point)
    return results

def convertPointsInBulk():
    convertCsvToPoints(converter.processAddress)

def convertCsvToPoints(callback):
    with open('sample-data.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        count = 0
        for row in data:
            count = count + 1
            callback(row, count)



if __name__ == "__main__":
    convertPointsIteratively()
    convertPointsInBulk()
