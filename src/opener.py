import csv
import re

def checker(file):
    path = file.split("\\")
    #print(path[-1])
    endpath = "\\".join(path[:-1]) 
    #print(endpath)
    return endpath

def opener(file):
    final = checker(file)
    print(final)
    try: 
        with open(file) as f:
            csv_reader = csv.DictReader(f, delimiter=";")
            lines = 0
            header = next(csv_reader,None)
            for row in csv_reader:
                #print(row)
                pass

        return
    except Exception:
        print("no se puede abrir el archivo")