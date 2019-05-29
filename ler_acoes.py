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
b = {}
with open("acoes.csv") as myfile:
    firstline = True
    for line in myfile:
        if firstline:
            mykeys = "".join(line.split()).split(',')

            firstline = False
        else:

            values = "".join(line.split()).split(',')
            print(mykeys)
            print(values)
            for n in range(0, len(mykeys)):
                dict1 ={mykeys[n]:values[n]}
                b.update(dict1)
                #b[mykeys[n]]=values[n]
                print(mykeys[n]+":"+values[n])
                print(b[mykeys[n]])
            #a.append({mykeys[n]:values[n] for n in range(0,len(mykeys))})
            print(b)
            a.append(b)
            b={}
print(a[30])

with open("acoes.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    C=[]
    for row in reader:
        print(row)
        print(dict(row))
        C.append( dict(row))
csvfile.close()
print("C [30][OPRD ="+C[30]['OPR'])