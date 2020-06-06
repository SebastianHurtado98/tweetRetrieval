from fileToStructure import *
import math
import collections

tweetIds = jsonToDict("idText.json")
df = jsonToDict("documentFrequency.json")
index = jsonToDict("index.json")


def queryWeightPerDoc(tokens):
    result = {}
    nTweets = len(tweetIds.keys())
    for token in tokens:
        if token in index.keys():
            counter = collections.Counter(tokens)
            frequencyInQuery = counter[token]
            tokenTotalFrequency = index[token]['frequency']
            q = math.log(1 + frequencyInQuery,2) * math.log(1 + 1/frequencyInQuery, 10)
            docs = index[token]['docs']
            for doc in docs:
                frequencyInDoc = docs[doc]
                d = math.log(2, 1 + frequencyInDoc) * math.log(nTweets/tokenTotalFrequency, 10)
                if doc in result.keys():
                    result[doc]['sum1'] = result[doc]['sum1'] + d*q
                    result[doc]['sum2'] = result[doc]['sum2'] + q*q 
                    result[doc]['sum3'] = result[doc]['sum3'] + d*d
                else:
                    result[doc] = dict()
                    result[doc]['sum1'] = d*q
                    result[doc]['sum2'] = q*q
                    result[doc]['sum3'] = d*d

    for doc in result.keys():
        sumA = result[doc]['sum1']
        sumB = math.sqrt(result[doc]['sum2']) * math.sqrt(result[doc]['sum3'])
        if sumB == 0:
            result[doc] = 0
        else:
            result[doc] = sumA / sumB
    return result

