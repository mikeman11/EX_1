import csv

from numpy import size


class Caller:

     def __init__(self ,time,src,dst,alocated):
       self.time = time
       self.src = src
       self.dst = dst
       self.alocated = alocated

     def __repr__(self):
         return  repr(self.time)
calls = []

file_path = "Ex1_Calls/Calls_a.csv"
with open(file_path) as f:
    reader = csv.reader(f)
    for row in reader:
        calls.append(Caller(row[1], row[2], row[3], row[4]))


print(size(calls))













