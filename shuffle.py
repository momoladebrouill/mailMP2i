import random

def x(i,l):
    a=random.randrange(0,len(l))
    while a==i:
        a=random.randrange(0,len(l))
    return l.pop(a)

def shuffle(elems):
    l=elems[:]
    nl=[]
    for i in range(len(elems)):nl.append(x(i,l))
    return nl

if __name__=="__main__":
    l=[i for i in range(10)]
    shuffled=shuffle(l)
    print(l)
    print(shuffled)
