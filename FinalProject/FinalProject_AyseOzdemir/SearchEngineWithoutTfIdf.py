import os
import time
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from string import punctuation

documentCount = 0
wordDict = {}
wordSet = set()
urlSet = set()
resultList = []

def EliminateStopWords(content):
    sw = stopwords.words("english") + list(punctuation)
    sw = [x.upper() for x in sw]
    for item in sw:
        content = content.replace(' ' + item, ' ')
    return content

def LoadDocument(documentName):
    global documentCount
    global wordDict

    with open(documentName) as f:
        soup = BeautifulSoup(f,features="html.parser")
        n1 = soup.findChild()
        p3 = len(soup.findChildren()) #total document count, required to calculate idf
        documentCount = p3
        tfidf = 0

        while n1:
            if len(n1) > 0:
                url = n1.attrs['url'] if 'url' in n1.attrs else ''
                title = n1.attrs['title'] if 'title' in n1.attrs else ''

                content = n1.contents[0]
                content = EliminateStopWords(content)
                tmpDict = content.split() #
                p2 = len(tmpDict)
                for item in tmpDict:
                    if item not in wordSet: #new word
                        p1= tmpDict.count(item)
                        p4 = p3
                        tfidf = ComputeTfIdf(p1, p2, p3, p4)
                        wordDict[item] = ([(tfidf, url, title)])
                        wordSet.add(item)
                        urlSet.add(str(item) + str(url))
                    else:  #already exist word
                        if str(item) + str(url) in urlSet:
                            continue
                        else:
                            wordDict[item].append([(tfidf,url,title)])
                n1 = n1.findNextSibling()
            else:
                n1 = n1.findNextSibling()

def Search(searchKey):
    global wordDict
    global resultList

    keySet = set(searchKey)

    resultList = (keySet & wordSet) #set intersection operation
    return resultList

def ComputeTf(p1, p2): #p1=number of key in text/p2=total number of words in text
    return p1 / float(p2)

def ComputeIdf(p3, p4): #p3=total number of documents/p4=number of documents has key
    return p3 / float(p4)

def ComputeTfIdf(p1, p2, p3, p4):
    return ComputeTf(p1, p2) * ComputeIdf(p3, p4)

if __name__ == '__main__':
    print('Welcome to the search engine!')

    while True:
        resultList = []
        print('type: ')
        script = input().split()
        command = script[0].strip()
        if command == 'load':
            fileName = script[1].strip()
            if not os.path.exists(fileName):
                print('File could not be found!')
                continue

            startTime =time.time()
            LoadDocument(fileName)
            endTime = time.time()
            print('Loaded {0} documents in {1} seconds.'.format(documentCount, int(endTime-startTime)))
        elif command == 'search':
            try:
                searchKey = script[1:]
            except:
                print('Please use the correct format!\nCorrect Format-> search <words>')

            startTime = time.time()
            resultList = Search(searchKey)
            endTime = time.time()
            print('Search completed in {0} seconds.'.format(int(endTime - startTime)))
            print('Titles,tfidf values and urls of matching documents:')

            if len(resultList) > 0:
                for result in resultList:
                    print('{:<40},{:<20}                   --> {:<10}'.format(wordDict[result][0][2],wordDict[result][0][0], wordDict[result][0][1]))
            else:
                resultList.append('No record found!')
        else:
            print('Wrong input format!')
    print('finished!')