import csv
from typing import TextIO
dataset = dict()
a = []
'''

with open('acoes.csv') as f:
    reader = csv.reader(f, skipinitialspace=True)
    #header = next(reader)
    #a = [dict(zip(header, map(int, row))) for row in reader]
    a = list(reader)
    a.
print (a[0][$])

with open('regramod.csv','r') as csv_file:
    data=csv.DictReader(csv_file)
    for line in data :
        a.append(line)
print(a)

print(a[0])

with open("regramod.csv") as myfile:
    for line in myfile:
        values = "".join(line.split()).split(',')
        a.append({values[0]:values[1]})
    firstline = True
    for line in myfile:
        if firstline:
            mykeys = "".join(line.split()).split(',')
            firstline = False
        else:
            values = "".join(line.split()).split(',')
            a.append({mykeys[n]:values[n] for n in range(0,len(mykeys))})



b = []
with open("regramod.csv") as myfile:
    firstline = True
    for line in myfile:
        if firstline:
            mykeys = "".join(line.split()).split(',')
            firstline = False
        else:
            values = "".join(line.split()).split(',')
            b.append({mykeys[n]:values[n] for n in range(0,len(mykeys))})
print(b[]['indice'])
'''
a = {}

with open("regra_nao_terminal.csv") as myfile:
    for line in myfile:
        values = "".join(line.split()).split(',')
        a.update({values[0]:values[1]})
print (a['3'])