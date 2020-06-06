import csv
import json
#run preprocessing for a new set of files

terminos = []

def csvToArray(fileName):
    inFile = open(fileName, "rU")
    reader = csv.reader(inFile, delimiter=";")

    array = []

    for row in reader:
        array.append (row)

    inFile.close()
    return array


def jsonToDict(fileName):
    with open(fileName) as json_file:
        data = json.load(json_file)
        return data

