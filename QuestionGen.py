PYTHONPATH =''
__author__ = 'jt306'
# import nltk
# from PIL import Image,ImageFont,ImageDraw
import urllib3
# from urllib3 import request
import urllib3.request
# from bs4 import BeautifulSoup
# from nltk import word_tokenize
# from nltk.corpus import stopwords
# from nltk.corpus import words
# # nltk.download()
# import csv
# import pickle
# from collections import defaultdict, Counter
# from Doge1 import make_doge
import sys
# print (sys.argv)
print(sys.version)
sys.path.append(r'/Volumes/LocalDataHD/j/jt/jt306/Downloads/LanguageEngineering')
import nltk.data
import sussex_nltk


# from HTMLParser import HTMLParser
#
# class MLStripper(HTMLParser):
#     def __init__(self):
#         self.reset()
#         self.fed = []
#     def handle_data(self, d):
#         self.fed.append(d)
#     def get_data(self):
#         return ''.join(self.fed)
#
# def strip_tags(html):
#     s = MLStripper()
#     s.feed(html)
#     return s.get_data()

#
# from nltk.parse.stanford import StanfordDependencyParser
# path_to_jar = 'path_to/stanford-parser-full-2014-08-27/stanford-parser.jar'
# path_to_models_jar = 'path_to/stanford-parser-full-2014-08-27/stanford-parser-3.4.1-models.jar'
# dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
#
# result = dependency_parser.raw_parse('I shot an elephant in my sleep')
# dep = result.next()
# list(dep.triples())


# print '\n-----\n'.join(tokenizer.tokenize(data))

def get_sentences(url):
    hdr = { 'User-Agent' : 'doge user agent' }
    req = urllib3.urlopen(url, headers=hdr)
    html = request.urlopen(req).read()
    paragraphs = BeautifulSoup(html,"lxml").text

    # paragraphs = str(soup.find_all('p'))

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences= (tokenizer.tokenize(paragraphs))     # returns a list of sentences
    # print (len(sentences))
    # print(type(sentences))
    return (sentences)

sentences = get_sentences('https://en.wikipedia.org/wiki/Henry_VIII_of_England')

def get_guestions(sentences):
    # for index, sentence in enumerate(sentences):
    #     print (index, sentence)
    list_of_is = ['is a ', 'is the', 'is an ', ' are ']
    list_of_because = ['because','due to', 'owing to']


    print('\n iterating over sentences:')
    for sentence in sentences:
        # for item in list_of_is:
        #     if item in sentence:
        #         print (sentence)
        #         index = sentence.find(item)
        #         print ('What '+sentence[index:-1]+'?\n')

        if 'because' in sentence:
            print ([word for word in sentence.split(' ')])
            sentence = ' '.join([word for word in sentence.split(' ') if '[' not in word])
            print(sentence)
            index = sentence.find('because')
            print ('Why is it that '+sentence[:index]+'?\n')

get_guestions(sentences)


    # if tokens[index + 1] in ['a', 'an', 'the']:
    #     end_of_sentence = tokens
    #     sentence = (tokens[index - 10:index + 10])  # makes a sentence around this word
    #     sentence2 = (tokens[index + 1:index + 10])
    #     # for word in sentence: if word is 'there'
    #     print('Sentence with word ->', ' '.join([word for word in sentence]))
    #     print('What is', ' '.join([word for word in sentence2]) + '?\n')

    # tokens = list(word for word in word_tokenize(paragraphs))  # if word.isalpha()) #tokens is the list of all words
    # indices = [i for i, x in enumerate(tokens) if x == 'is'] # looks for the word 'is'
    # for sentence in sentences:""
    # # for index in indices:
    #     if tokens[index+1] in ['a','an','the']:
    #         end_of_sentence = tokens
    #         sentence = (tokens[index-10:index+10])  #makes a sentence around this word
    #         sentence2 = (tokens[index+1:index+10])
    #         # for word in sentence: if word is 'there'
    #         print ('Sentence with word ->',' '.join([word for word in sentence]))
    #         print('What is', ' '.join([word for word in sentence2])+'?\n')

    # if 'is a' in paragraphs:
    #     print ('found!')
    #     print (paragraphs[paragraphs.find('is a')-20:paragraphs.find('is a')+20])






