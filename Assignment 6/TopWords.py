# topwords.py
# Function to compute the list of top N words
# in a file. Words with same frequency are ordered
# alphabetically.
# Input Parameters: FILE (file object), N (number of words to return)
# Return Value: top_words (list of top N words)
# May need separate library files for each version of python

import collections

def TopWords(FILEOBJECT, N): 
    # get the sequence of words from the file
    text = FILEOBJECT.read()
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~' + "'":
        text = text.replace(ch, ' ')
    words = text.split()

    #construct a Counted dictionary of word counts
    counts = collections.Counter(words)
    dict1 = dict(counts)

    #Sort the dictionary, primary key = word frequency
    #secondary key = alphabetical order
    sort1= sorted(dict1.items(), key=lambda item: item[0])
    sort2=sorted(sort1, key=lambda item: item[1], reverse=True)

    #construct a list of top N words
    top_words=[]

    for index in range(N):
        top_words.append(sort2[index][0])

    return top_words

