# -*- coding: utf-8 -*-
"""NLP4(KunalChauhan).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GJzXkq221AoPxIw43jbSCUfDsgppg2P9
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist

def summarize_text(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    
    # Calculate word frequencies
    word_frequencies = FreqDist()
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence):
            if word.lower() not in stop_words:
                word_frequencies[word.lower()] += 1
    
    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence):
            if word.lower() in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word.lower()]
                else:
                    sentence_scores[sentence] += word_frequencies[word.lower()]
    
    # Select top sentences with highest scores
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    # Join selected sentences to create the summary
    summary = ' '.join(top_sentences)
    
    return summary

# Read the text file
with open('samplestory.txt', 'r') as file:
    text = file.read()

# Perform text summarization
summary = summarize_text(text, num_sentences=3)
print(summary)