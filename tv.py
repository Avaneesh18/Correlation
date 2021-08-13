import csv
import numpy as np

def getDataSource(data_path):
    size_of_tv = []
    average_time_spent = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            size_of_tv.append(float(row["size of tv"]))
            average_time_spent.append(float(row["\t AVERAGE TIME SPENT WATHING TV IN A WHEEK"]))

    return{"x": size_of_tv, "y":average_time_spent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between size of tv and average time spent: \n ",correlation[0,1])

def setup():
    data_path = "Data/Size of TV,_Average time spent watching TV in a week (hours).csv"
    datasource = getDataSource(data_path)

    findCorrelation(datasource)

setup()