#Homework for Algorithm Design 1, week 5,
#implement dijkstra algorithm with heap

import heapq

global n
n = 200

def readin():
    global n 
    data = open('G:\\UCHI\Algorithm design 1\week5\dijkstra.txt', 'r')
    datalist = list(data)
    adlist = [[] for i in range(n)]
    weight = [[] for i in range(n)]
    for i in datalist:
        temp = i.split()
        tail = int(temp.pop(0))
        while temp:
            tempnode = temp.pop(0).split(',')
            adlist[tail - 1].append(int(tempnode.pop(0)))
            weight[tail - 1].append(int(tempnode.pop(0)))
    return(adlist, weight)

def unique_index(L,e):
    return [i for i,j in enumerate(L) if j[1] == e]

def heapreplace(H, pos, new):
    if H[pos][0] <= new:
        return(H)
    else:
        H[pos] = (new, H[pos][1])
        while pos > 0 and H[pos] < H[pos // 2]:
            temp = H[pos]
            H[pos] = H[pos // 2]
            H[pos // 2] = temp
            pos = pos // 2
        return(H)

def dijkstra(edges, weight):
    X = [1]
    A = [1000000 for i in range(n)]
    A[0] = 0
    H = []
    for i in range(len(edges[0])):
        H.append((weight[0][i], edges[0][i]))
    heapq.heapify(H)
    while len(X) < n and H is not []:
        #print(str(H))
        #print(str(A) + '\n')
        new = heapq.heappop(H)
        X.append(new[1])
        A[new[1] - 1] = new[0]
        for j in range(len(edges[new[1] - 1])):
            if edges[new[1] - 1][j] not in X:
                pos = unique_index(H, edges[new[1] - 1][j])                                                    #新点是否在H中
                if pos == []:
                    heapq.heappush(H, (weight[new[1] - 1][j] + new[0], edges[new[1] - 1][j]))
                elif len(pos) > 1:
                    print('error----pos = ' + str(pos))
                else:
                    H = heapreplace(H, pos.pop(), new[0] + weight[new[1] - 1][j])                        #已在H中，考虑是否替换
                    H1 = heapq.heapify(H)
                    if str(H[0]) != str(H[0]):
                        print('error')
    return(A)
                    
(edges, weight) = readin()
A = dijkstra(edges, weight)
print(A[6], A[36], A[58], A[81], A[98], A[114], A[132], A[164], A[187], A[196])
