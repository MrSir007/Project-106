import csv
import numpy as np

def getData (datapath) :
  # To convert ice-cream data and sales data into lists
  coffeecups = []
  sleephours = []

  with open (datapath) as data :
    dataReader = csv.DictReader(data)
    # To convert string value into float value
    for row in dataReader :
      coffeecups.append(float(row["Coffee in ml"]))
      sleephours.append(float(row["sleep in hours"]))
  
  return {"x": coffeecups, "y": sleephours}

def findCorrelation (datasource) :
  correlation = np.corrcoef(datasource["x"],datasource["y"])
  print("The correlation is", correlation[0,1])

def main () :
  datapath = "cups of coffee vs hours of sleep.csv"
  datasource = getData(datapath)
  findCorrelation(datasource)

main()