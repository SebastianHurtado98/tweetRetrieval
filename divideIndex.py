from fileToStructure import *
import json

#necesitar partir el indice en varios archivos para subirlo a github.
#el tiempo de generacion del indice demora aprox 2 horas. Es mejor tenerlo en archivo.
index = jsonToDict("index.json")
nElements = len(index.keys())
#nElements = 161220. Vamos a dividir según la distribución (hay elementos que pesan más que otros, y estos están al principio)

newIndexA = {}
newIndexB = {}
newIndexC = {}
newIndexD = {}

counter = 0
for i in index:
    if counter < 100:
        newIndexA[i] = index[i]
    else:
        if counter < 2500:
            newIndexB[i] = index[i]
        else:
            if counter < 40000:
                newIndexC[i] = index[i]
            else:
                newIndexD[i] = index[i]
    counter = counter + 1

with open('indexA.json', 'w') as outfile:
    json.dump(newIndexA, outfile)

with open('indexB.json', 'w') as outfile:
    json.dump(newIndexB, outfile)

with open('indexC.json', 'w') as outfile:
    json.dump(newIndexC, outfile)

with open('indexD.json', 'w') as outfile:
    json.dump(newIndexD, outfile)
