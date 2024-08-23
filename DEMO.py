import csv
def ID_CHECK():
    f=open("ID.csv","r")
    wr=csv.reader(f)
    for row in wr:
        print(row)
ID_CHECK()
