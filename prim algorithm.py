#Q3 for Algorithm design 2, prim algorithm for MST, with heap

import string
import heapq
import re

def unique_index(L,e):
    return [i for i,j in enumerate(L) if j == e]

data = open('G:\\UCHI\Algorithm design 2\week1\Q3.txt', 'r')
size = data.readline().split()
nedges = int(size.pop())
nnodes = int(size.pop())
datalist = list(data)
nodes1 = []                                  #beginning nodes
nodes2 = []                                  #ending nodes
edgecosts = []                            #costs of edges

for i in datalist:
    temp = i.split()
    edgecosts.append(int(temp.pop()))
    nodes2.append(int(temp.pop()))
    nodes1.append(int(temp.pop()))

X = []                                              #completed nodes
heap = []
Tnodes1 = []                               #beginning nodes of completed paths
Tnodes2 = []                               #ending nodes of completed paths
Tcosts = []                                   #costs of completed paths

X.append(1)                                #node 1 is the initial node

while len(X)<nnodes:
    new = X[len(X)-1]
    for i in unique_index(nodes1,new):
        aim = nodes2[i]
        if aim in X:
            continue
        else:
            m=0
            for j in range(len(heap)):
                if heap[j][2] == aim:
                    m=1
                    if edgecosts[i]<heap[j][0]:
                        del heap[j]
                        heapq.heappush(heap, (edgecosts[i], new, aim))
                        break
            if m == 0:
                    heapq.heappush(heap, (edgecosts[i], new, aim))
                            
    for i in unique_index(nodes2,new):
        aim = nodes1[i]
        if aim in X:
            continue
        else:
            m=0
            for j in range(len(heap)):
                if heap[j][2] == aim:
                    m=1
                    if edgecosts[i]<heap[j][0]:
                        del heap[j]
                        heapq.heappush(heap, (edgecosts[i], new, aim))
                        break
            if m == 0:
                    heapq.heappush(heap, (edgecosts[i], new, aim))
        
    heapq.heapify(heap) 
    temp = heapq.heappop(heap)
    Tnodes1.append(temp[1])
    Tnodes2.append(temp[2])
    Tcosts.append(temp[0])
    X.append(temp[2])
    
    
