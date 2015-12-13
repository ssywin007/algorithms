#Q2 for Algorithm design 1, week 2. QuickSort and the key is the last element in the array


data = open('G:\\UCHI\Algorithm design 1\week2\Q1.txt', 'r')
datalist = list(data)
size = len(datalist)
array = []

for i in datalist:
    array.append(int(i.strip()))

p = [(0,size)]                                        #a list of tuples with the beginning and ending position of  each unsorted partition
comparison = 0

def swap(array, i, j):
    tempnum = array[j]
    array[j] = array[i]
    array[i] = tempnum
    return(array)

def QuickSort(array, tempbegin, tempend):
    array = swap(array, tempbegin, tempend - 1)
    key = array[tempbegin]
    i = tempbegin + 1
    j = tempbegin + 1
    while j < tempend:
        if array[j] < key:
            array = swap(array, i, j)
            i += 1
        j += 1
    array = swap(array, tempbegin, i-1)
    return(array, i-1)

while p != []:
    current = p.pop(0)
    tempbegin = current[0]
    tempend = current[1]
    comparison += tempend - tempbegin - 1
    (array, keyp) = QuickSort(array, tempbegin, tempend)
    if tempend - keyp > 2:
        p.insert(0, (keyp + 1,tempend))
    if keyp - tempbegin > 1:
        p.insert(0, (tempbegin, keyp))
    

