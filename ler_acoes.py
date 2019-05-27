import csv
from typing import TextIO
dataset = dict()
'''

with open('acoes.csv') as f:
    reader = csv.reader(f, skipinitialspace=True)
    #header = next(reader)
    #a = [dict(zip(header, map(int, row))) for row in reader]
    a = list(reader)
    a.
print (a[0][$])

with open('acoes.csv','r') as csv_file:
    data=csv.DictReader(csv_file)
    a=list(data)
'''
a = []
with open("acoes.csv") as myfile:
    firstline = True
    for line in myfile:
        if firstline:
            mykeys = "".join(line.split()).split(',')
            firstline = False
        else:
            values = "".join(line.split()).split(',')
            a.append({mykeys[n]:values[n] for n in range(0,len(mykeys))})
print(a[0])