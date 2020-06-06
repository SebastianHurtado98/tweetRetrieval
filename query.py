from index import *
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from fileToStructure import *

idText = jsonToDict("idText.json")


#se agrega la función acá para que no ejecutar preprocessing solo por esta función
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

def query(sentence):
    tokens = preprocessing(sentence)
    result = queryWeightPerDoc(tokens)
    return result

def topTen(q):
    top = {}
    result = query(q)
    sortedResult = sorted(result.items(), key=lambda kv: kv[1], reverse= True)
    if len(sortedResult) > 10:
        for i in range(10):
            top[sortedResult[i][0]] = idText[sortedResult[i][0]]
    else:
        for i in sortedResult:
            top[sortedResult[i][0]] = idText[sortedResult[i][0]]

    counter = 1
    for i in top.keys():
        print("Tweet N" + str(counter) + ": ")
        print(top[i])
        print("\n")
        counter = counter + 1
    print("Fin de la búsqueda. \n")
    
