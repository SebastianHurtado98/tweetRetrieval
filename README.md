# Databases II - Project 2 - Part 1
Implementation of an inverted index for text retrieval, using the ranked information retrieval model for natural language queries. We are considering the following steps:

## Preprocessing
* Tokenization
* Stopwords filtering
* Stemming

## Index building
* Using cosine similarity with Term Frequency - Inverse Document Frequency weight.
* It can be stored in secondary memory.

## Query
* Proposal of three different queries and showing the **top 10 tweets** that approximate each query.
* The queries are one or more words in natural language.

To analyze the perforamnce of the implementation, a collection of approximately 20 000 tweets is provided. 

* The dictionary of terms is build upon the `text` attribute.
* `docID` represents the ID of the tweet.

After performance analysis, there's a proposal of an algorithmic solution for the use of secondary memory with big data collections.
