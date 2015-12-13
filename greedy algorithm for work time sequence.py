#Q2 for Algorithm design 2, greedy algorithm for work time sequence

import string


def unique_index(L,e):
    return [i for i,j in enumerate(L) if j == e]

data = open('G:\\UCHI\Algorithm design 2\Q1.txt', 'r')
size = data.readline()
size = int(size)
datalist = list(data)
weight = []
length = []
ratio = []                           #weight/length
rank = []                           #descending sequence of ratio
lengthseq = []
weightseq = []
completetseq = []
total = []

for i in datalist:
    temp = i.split()
    temp1 = temp.pop()
    temp2 = temp.pop()
    length.append(int(temp1))
    weight.append(int(temp2))
    ratio.append(int(temp2)/int(temp1))

rank = list(set(ratio))
rank.sort()
rank.reverse()

if len(datalist) != size or len(length) != size or len(weight) != size or len(ratio) != size:
    print('There are some mistakes with the dimension of the data')

for i in rank:
    tempweightseq = []
    templengthseq = []
    for j in unique_index(ratio, i):
        tempweightseq.append(weight[j])
    tempweightseq.sort()
    tempweightseq.reverse()
    for j in tempweightseq:
        templengthseq.append(j/i)
    weightseq.extend(tempweightseq)
    lengthseq.extend(templengthseq)

if len(weightseq) != size or len(lengthseq) != size:
    print('There are some mistakes with the dimension of the data')
        
for i in range(len(lengthseq)):
    completetseq.append(sum(lengthseq[:i+1]))
    total.append(completetseq[i]*weightseq[i])

ttotal = sum(total)

        
        
    






