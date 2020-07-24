from TopWords import *

def CompareWords(File1Dict, File2Dict):
    wordmatch=0
    for words1 in File1Dict:
        for words2 in File2Dict:
            if words1==words2:
                wordmatch=wordmatch+1
    return (wordmatch)
                       

def main(): 
    textA=open(input("Name of first text:"),"r")
    textB=open(input("Name of second text:"),"r")
    N=int(input("Enter number of top words to compare:"))
    x=TopWords(textA,N)
    y=TopWords(textB,N)
    common_words=CompareWords(x, y)
    common_words=(common_words)
    percent=common_words/N
    print ("Number of words in common:", common_words)
    print ("Percentage of words in common:", percent)

    
main()
