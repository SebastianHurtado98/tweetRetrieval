from fileToStructure import *
import json

#necesitar unir los indices que se pueden subir a github.
#el tiempo de generacion del indice demora aprox 2 horas. Es mejor tenerlo en archivo.
#nElements = 161220. 

newIndexA = jsonToDict("indexA.json")
newIndexB = jsonToDict("indexB.json")
newIndexC = jsonToDict("indexC.json")
newIndexD = jsonToDict("indexD.json")

index = {}

for i in newIndexA:
    index[i] = newIndexA[i]
for i in newIndexB:
    index[i] = newIndexB[i]
for i in newIndexC:
    index[i] = newIndexC[i]
for i in newIndexD:
    index[i] = newIndexD[i]


with open('index.json', 'w') as outfile:
    json.dump(index, outfile)



