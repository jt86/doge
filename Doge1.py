__author__ = 'jt306'
import nltk
from PIL import Image,ImageFont,ImageDraw
from urllib import request
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import words
# nltk.download()
from nltk.stem import PorterStemmer
import csv
import pickle
from collections import defaultdict, Counter
from random import shuffle





tokens = nltk.corpus.gutenberg.words('melville-moby_dick.txt')

def make_doge(article_num):
    with open('listofwords{}.csv'.format(article_num),'rb') as file:
        tokens =  pickle.load(file)
    list1=['javascript','expand','point','return','togglecomment','void','time','tagline','author','parent','userattrs','utc','mon','feb','percent','list','today','sup','reference','way','thing','nofollow','ltr','font','imagecaption','link','amp','http','body','subreddit','comment','man', 'woman', 'news','ago', 'input','children', 'permalinksaveparentreportgive', 'goldreply', 'hidden', 'minutes', 'score', 'points', 'comments', 'hour', 'option', 'goldreplyload', 'replies', 'reply', 'child', 'permalinksavereportgive', 'div', 'load', 'span', 'years', 'like', 'think', 'https', 'even', 'would', 'still', 'post', 'get',  'password', 'happened','label', 'back']
    tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stopwords.words('english') and word.lower() not in list1 and len(word)>2]# and word in words.words()]
    print (tokens)

    counts = Counter(tokens)
    common_words= (counts.most_common(50))
    common_words = [word for word in common_words if 'NN' in (nltk.pos_tag([word[0]])[0])]
    print (common_words)
    word1,word2,word3,word4,word5,word6 = common_words[0][0],common_words[1][0],common_words[2][0], \
                                          common_words[3][0], common_words[4][0], common_words[5][0],

    rgb_codes = [(141,221,0),(476,22,179),(252,61,49),(250,250,60),(255,83,0),(0,169,252)]
    shuffle(rgb_codes)
    locations = [(40, 0),(10, 35),(15, 80),(10, 140),(140, 110)]
    shuffle(locations)

    img = Image.open('doge.jpeg')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Comic Sans MS.ttf',20)
    draw.text(locations[0],"very {}".format(word1),rgb_codes[0],font=font)
    draw.text(locations[1],"so {}".format(word2),rgb_codes[1],font=font)
    draw.text((250, 20),"wow {}".format(word3),rgb_codes[2],font=font)
    draw.text(locations[2],"many {}".format(word4),rgb_codes[3],font=font)
    draw.text(locations[3],"such {}".format(word5),rgb_codes[4],font=font)
    draw.text(locations[4],"much {}".format(word6),rgb_codes[5],font=font)
    img.save('sample-out.png')
    img.show()

def get_listofwords(url,num):
    hdr = { 'User-Agent' : 'doge user agent' }
    req = request.Request(url, headers=hdr)
    html = request.urlopen(req).read()
    soup = BeautifulSoup(html,"lxml")
    paragraphs = str(soup.find_all('p'))
    tokens = word_tokenize(paragraphs)

    with open('listofwords{}.csv'.format(num),'wb') as file:
        pickle.dump(tokens,file)


get_listofwords('http://www.bbc.co.uk/news/election-us-2016-37332106',16)
make_doge(16)
