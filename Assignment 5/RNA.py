def main (): 
    RNA1=['A','U','G','U','G','G','G','U','C','C','A','C','G','A','C','U','C','G','U','C','G','U','C','U','A','C','U','A','G','A'] 

    RNA2=['C','U','G','A','C','G','A','C','U','A','U','A','A','G','G','G','U','C','A','A','G','C']
    MatchSequences(RNA1, RNA2)
    RNA=RNA1
    start1=3
    end1=14
    start2=28
    end2=17
    MatchRNA(RNA, start1, end1, start2, end2)
    MatchRNA(RNA, 3, 14, 28, 17)
    MatchRNA(['A','U','G','U','G','G','G','U','C','C','A','C','G','A','C','U','C','G','U','C','G','U','C','U','A','C','U','A','G','A'], 3, 14, 28, 17)
    RNAseq_match=MatchRNA(RNA, start1, end1, start2, end2)
    print(RNAseq_match)

def MatchSequences(RNA1, RNA2):
    zip(RNA1, RNA2)
    match={'A':'U', 'U':'A', 'C':'G', 'G':'C'}
    matches=0
    if len(RNA1)>len(RNA2):
        short=RNA2
    else:
        short=RNA1
        
    for i in range(len(short)):
        if match[RNA1[i]]==RNA2[i]:
            matches=matches+1
    print(matches)
        
def MatchRNA(RNA, start1, end1, start2, end2):
    RNA[4:].reverse()

main()

#matches in this order 2,3,4,4
