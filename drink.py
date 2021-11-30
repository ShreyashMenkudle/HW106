import csv 
import numpy as np

def setup():
    dataPath = "stimulant.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

def getDataSource(data_path):
    consumption = []
    sleepTimes = []
    with open (data_path) as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            consumption.append(float(row["Coffee in ml"]))
            sleepTimes.append(float(row["sleep in hours"]))
    return {"x":consumption,"y":sleepTimes}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"]) 
    print("Correlation between TV Size and TV time :- \n--->",correlation[0,1])
setup()