import csv
import xml.etree.ElementTree as ET
from src.organismos import organismos,validate


def main():
    path = input("donde esta el archivo?")
    #print(path)
    name = input("nombre archivo 2")
    organismos(path,name)
    validate()

if __name__ == "__main__":
    main()