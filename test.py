from fileToStructure import *

#Prueba la correctitud del divide y merge.

index = jsonToDict("index.json")
indexTest = jsonToDict("indexTest.json")

print(len(index.keys()))
print(len(indexTest.keys()))