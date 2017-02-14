PYTHONPATH =''
__author__ = 'jt306'

# import urllib3
#
import urllib.request
import nltk
# from bs4 import BeautifulSoup
#
# import sys
# # print (sys.argv)
# print(sys.version)
# sys.path.append(r'/Volumes/LocalDataHD/j/jt/jt306/Downloads/LanguageEngineering')
# import nltk.data
#
#
import sys
print(sys.version)
from bs4 import BeautifulSoup
import urllib
r = urllib.request.urlopen('https://therunningbug.com/training/marathon-plans/16-week-intermediate-marathon-training-plan').read()
soup = BeautifulSoup(r,'lxml')
print (type(soup))

print(soup)

days = soup.find_all(class_="activity-plan__interval__heading")
lengths = soup.find_all(class_="activity-plan__instructions__summary plan__instructions__summary--duration")
descriptions = soup.find_all(class_="activity-plan__instruction")
activities = soup.find_all(class_="activity-plan__instruction__label")


for day, activity, length, description in zip(days,activities,lengths,descriptions):
    print([item.get_text() for item in [day, activity,length,description]])


# for item in soup:
#     print(type(item))

# paragraphs = str(soup.find_all('p'))
# tokens = nltk.word_tokenize(paragraphs)

#
# print(len(tokens))
# print((tokens)[500:])

# for i in range(len(tokens)):
#     print (tokens[i:i + 7])


# for count,item in enumerate(tokens):
#     if count%5:#==0:
#         print(count,item)
