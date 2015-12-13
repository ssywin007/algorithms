#Q1 for Algorithm design 1, week 1. Divide & Conquer for # of inversion

import string

def unique_index(L,e):
    return [i for i,j in enumerate(L) if j == e]

#merge algorithm
def merge(a,b):
    c = []
    count = 0
    i = 0
    j = 0
    imax = len(a)
    jmax = len(b)
    for k in range(imax + jmax):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            count = count + imax - i
        if i == imax:
            c += b[j:]
            break
        elif j == jmax:
            c += a[i:]
            break
    return (c, count)               

data = open('G:\\UCHI\Algorithm design 1\week1\Q1.txt', 'r')
datalist = list(data)
size = len(datalist)
array = []
inversion = 0

for i in datalist:
    array.append(int(i.strip()))

#record the position of division
div = [i for i in range(size + 1)]
narray = []
ndiv = [0]

while len(div) > 2:
    while len(div) > 2:
        (temp1, temp2) = merge(array[div[0] : div[1]], array[div[1] : div[2]])
        narray += temp1
        inversion += temp2
        ndiv.append(div[2])
        del div[0:2]
    if len(div) == 1:
        array = narray
    elif len(div) == 2:
        array = narray + array[div[0] : div[1]]
    narray = []
    div = ndiv + div[1:]
    ndiv = [0]
