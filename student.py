import csv
import numpy as np

def getData (datapath) :
  # To convert ice-cream data and sales data into lists
  studentmarks = []
  dayspresent = []

  with open (datapath) as data :
    dataReader = csv.DictReader(data)
    # To convert string value into float value
    for row in dataReader :
      studentmarks.append(float(row["Marks In Percentage"]))
      dayspresent.append(float(row["Days Present"]))
  
  return {"x": studentmarks, "y": dayspresent}

def findCorrelation (datasource) :
  correlation = np.corrcoef(datasource["x"],datasource["y"])
  print("The correlation is", correlation[0,1])

def main () :
  datapath = "Student Marks vs Days Present.csv"
  datasource = getData(datapath)
  findCorrelation(datasource)

main()