from collections import defaultdict
import glob
import os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 
import time

start = time.clock()
def create_index(data):
    index = defaultdict(list)
    for i, tokens in enumerate(data):
        for token in tokens:
            index[token].append(i)
    return index


def docFromFile(fname):
    doc = []
    with open(fname) as f:
        content = f.readlines()
    # Remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    for paragraph in content:
        wordList = paragraph.split(' ')
        for word in wordList:
            word = word.lower()
            for r in['.', ',', ';', ':']:
                if word.endswith(r):
                    word = word[: - 1]
            if word != "":
                doc.append(word)
    return doc

    

termList = []
os.chdir("docs/")
def postinglist():
    x = 0
    for file in glob.glob("*.txt"):
        termList.append(docFromFile(file))
        x += 1
    #print(termList)
    # print(index.keys())

def postinglistmp():
    pool = ThreadPool(8)
    termList = pool.map(docFromFile,glob.glob("*.txt"))
    #print(termList)


def search(data1):

    index = create_index(termList)
    posting_list1 = set(index[data1.lower()])
    return posting_list1

def search2(data2):

    index = create_index(termList)
    posting_list2 = set(index[data2.lower()])
    return posting_list2

def searchop(posting_list1,posting_list2):
#add more operation like or,maybe near search
    posting_listres = posting_list1 & posting_list2
    return posting_listres



#postinglist()
postinglistmp()
# # s1 = input("First term: ")
# # s2 = input("Second term: ")

s1 = "brother"
s2 = "water"
#posting_list1 = search(s1)
#posting_list2 = search2(s2)
#posting_listres = searchop(posting_list1,posting_list2)

stop = time.clock()

#print("Term1: ", s1, " ", posting_list1)
#print("Term2: ", s2, " ", posting_list2)
#print("Result: ", posting_listres)

print(str(stop-start)+"s") #printtime
