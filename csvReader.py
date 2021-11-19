import csv
import numpy as np


file = "Ex1_Calls/Calls_a.csv"
arrayofcall = np.zeros(5)

def readcsv(file:str):

    with open(file,) as f:


        r = csv.reader(f)
        for row in r:
            arrayofcall[0] =  row[1]
            arrayofcall[1] =  row[2]
            arrayofcall[2]  =  row[3]
            arrayofcall[3] = row [4]
            arrayofcall[4] = row[5]
            print(arrayofcall)


array = readcsv(file)
