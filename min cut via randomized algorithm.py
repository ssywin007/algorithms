#Homework for Algorithm Design 1, week 3, using randomized contraction algorithm to solve the min cut problem

import random


def readin():
    data0 = open('G:\\UCHI\Algorithm design 1\week3\Q1.txt', 'r')
    datalist = list(data0)
    size = len(datalist)
    adlist = []
    for i in range(size):
        tempd = []
        temp = datalist.pop(0).split()
        while temp:
            tempd.append(int(temp.pop(0)))
        tempd.pop(0)
        adlist.append(tuple(tempd))
    return(adlist)

def unique_index(L,e):
    return [i for i,j in enumerate(L) if j == e]

def exchange(tempdata2, tempnodes2, pos1, pos2):
    u2 = tempnodes2[pos1]
    v2 = tempnodes2[pos2]
    tempdata2[pos1].extend(tempdata2[pos2])
    for m in range(len(tempdata2)):
        n = unique_index(tempdata2[m], v2)
        while n:
            tempdata2[m][n.pop()] = u2
    h = unique_index(tempdata2[pos1], u2)
    while h:
        tempdata2[pos1].pop(h.pop())
    tempdata2.pop(pos2)
    tempnodes2.pop(pos2)
    return(tempdata2, tempnodes2)

def merge(tempnodes1, tempdata1, ss1):
    random.seed(ss1)
    numm = 0
    for k in tempdata1:
        numm += len(k)
    edge = random.randint(1,numm)
    posu = 0
    for l in tempdata1:
        if edge - len(l) <= 0:
            break
        edge -= len(l)
        posu += 1
    u = tempnodes1[posu]
    v = tempdata1[posu][edge - 1]
    posv = tempnodes1.index(v)
    if len(tempdata1[posu]) > len(tempdata1[posv]):
        (tempdata1, tempnodes1) = exchange(tempdata1, tempnodes1, posu, posv)
    else:
        (tempdata1, tempnodes1) = exchange(tempdata1, tempnodes1, posv, posu)
    return(tempnodes1, tempdata1)

def mincutalg(tempdata, tempnodes, ss):
    while len(tempdata) > 2:
        (tempnodes, tempdata) = merge(tempnodes, tempdata, ss)    
    return(len(tempdata[0]))

data = readin()
size = len(data)
nodes = [x + 1 for x in range(size)]
mincut = size
for i in range(size * size * 5):
    tdata = []
    for j in data:
        tdata.append(list(j))
    tnodes = []
    tnodes.extend(nodes)
    mincut = min(mincut, mincutalg(tdata, tnodes, i))
    


