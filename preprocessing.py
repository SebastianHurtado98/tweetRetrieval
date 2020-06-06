from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from fileToStructure import *
import json
import os
import csv

#este file se corre una vez para obtener el preprocessing de las json
#podrían haber algunos problemas con la lista terminos. Parece que es una lista dentro de otra lista de manera redundante.
# ¿terminos = terminos[0]? redundancia


#Se podría dividir el programa en más funciones. No se hace esto porque:
#1. Van a haber múltiples llamada (por tweet por word) a múltiples funciones.
#Esto es costoso
#2. Es legible de todas formas.

#Preprocessing es para crear los csv necesarios para la primera parte del proyecto

#funcion que quita stopwords, saca tokens y raíces. Devuelve un array de los terminos en un tweet
def preprocessing(tweet):
    sw = set(stopwords.words('spanish')) 
    tokens = word_tokenize(tweet) 
    
    words = [] 
    stemmer = PorterStemmer()

    for token in tokens:
        if token not in sw: 
            token = stemmer.stem(token)
            words.append(token) 
    return words
    

#inicializar estructuras para almacenar informacion
entries = os.listdir('parse/')
allData = []
terminos = []
ids = []
idTerminos = {}
idText = {}

#buscar en todos los json de tweets
for entrie in entries:
    with open('parse/' + entrie) as json_file:
        data = json.load(json_file)
        allData.append(data)

#preprocessing a cada tweet.
#se almacena el vector de terminos no repetidos como un csv
#se almacena el id del tweet con una lista de terminos como un json
#se almacena el id con el texto completo para la muestra de resultados final
#esto agiliza la lectura
for data in allData:
    for tweet in data:
        idText[tweet['id']] = tweet['text']
        i = tweet['id']
        text = tweet['text']        
        terms = preprocessing(text)
        idTerminos[i] = terms
        terms = set(terms)
        for term in terms:
            terminos.append(term)


termsFile = open("terminos.csv", "w") 
terminos = set(terminos)

#escribe el csv separado por ;
for term in terminos:
    termsFile.write(term)
    termsFile.write(";")
termsFile.close() 

#escribe el json
with open('idTerminos.json', 'w') as outfile:
    json.dump(idTerminos, outfile)

#sacar la frecuencia de documentos por cada termino
df = {}

for term in terminos: 
    df[term] = 0

for tweetKey in idTerminos.keys():
    for t in idTerminos[tweetKey]:
        if t in df.keys():
            df[t] = df[t] + 1

with open('documentFrequency.json', 'w') as outfile:
    json.dump(df, outfile)

with open('idText.json', 'w') as outfile:
    json.dump(idText, outfile)


#obtener el indice 

#id del texto con cada token (igual verifica si el token está)
tweetIds = jsonToDict("idTerminos.json")
#frecuencia de cada token
df = jsonToDict("documentFrequency.json")
#id y tweet
idText = jsonToDict("idText.json")
#terminos (esta en lista[0])
tokens = csvToArray("terminos.csv")


index = {}
nIds = len(tweetIds.keys())
counter = 0
for i in tweetIds:
    for j in tweetIds[i]:
        if j in tokens[0]:
            print(str(counter) + "out of " + str(nIds) + "\n")
            if j in index:
                index[j]['docs'][i] = 1
            else:
                base_dict = {'token': j, 'frequency': df[j], 'docs': dict()}
                index[j] = base_dict
    counter = counter + 1

with open('index.json', 'w') as outfile:
    json.dump(index, outfile)