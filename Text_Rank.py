#!/usr/bin/env python
# coding: utf-8


# Import the necessary libraries

from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx



# Building vocabulary and finding sentence similarity using "Cosine Distance"
 
def sent_similarity(s1, s2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    s1 = [word.lower() for word in s1]
    s2 = [word.lower() for word in s2]
 
    vocab = list(set(s1 + s2))
 
    vector1 = [0] * len(vocab)
    vector2 = [0] * len(vocab)
 
    # build the vector for the first sentence
    for word in s1:
        if word in stopwords:
            continue
        vector1[vocab.index(word)] += 1
 
    # build the vector for the second sentence
    for word in s2:
        if word in stopwords:
            continue
        vector2[vocab.index(word)] += 1
 
    return 1 - cosine_distance(vector1, vector2)

# Building similarity matrix between sentences

def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for index1 in range(len(sentences)):
        for index2 in range(len(sentences)):
            if index1 == index2: #ignore if both are same sentences
                continue 
            similarity_matrix[index1][index2] = sent_similarity(sentences[index1], sentences[index2], stop_words)

    return similarity_matrix

# Output the summarised text

def summary(file_name):
    print("in summary")
    top_n=5
    stop_words = stopwords.words('english')
    summarized_text = []
    file_name_edit = file_name.split(".")
    sentences =[]
    for sentence in file_name_edit:
        # print(sentence)
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    print(sentences)
    # Calling the respective functions

    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Ranking the sentences by building a graph using the "Networkx" library

    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    rank = nx.pagerank_numpy(sentence_similarity_graph)

    # Sorting the ranked sentences

    ranked_sentence = sorted(((rank[i],s) for i,s in enumerate(sentences)))    
    #print("Indexes of top ranked_sentence order are ", ranked_sentence)    
    for j in range(top_n):
        summarized_text.append(" ".join(ranked_sentence[j][1]))

    print("Summarized Text: \n", ". ".join(summarized_text))


# summary("sample.txt", 3)
