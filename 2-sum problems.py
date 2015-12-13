#Homework for Algorithm Design 1, week 6,
#solving 2-sum problems via hash map

def readin():
    data = open('G:\\UCHI\Algorithm design 1\week6\Q1.txt', 'r')
    datalist = list(data)
    input_array = []
    for i in datalist:
        input_array.append(int(i))
    return(input_array)

#detect a num is prime or not
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

#generate a prime bigger than the input 
def gen_prime(n):
    for i in range(n, 2 * n + 1):
        if is_prime(i) is True:
            return(i)
    return False
        
def unique_index(L,e):
    return [i for i,j in enumerate(L) if j[1] == e]

def hash_func(i, n):
    code = i % n
    return code

input_array = readin()
s = len(input_array)
if gen_prime(s) is not False:
    n = gen_prime(s)
else:
    n = s + 1
hashmap = [[] for i in range(n)]
target = [i for i in range(-10000, 10001)]
for i in input_array:
    code = hash_func(i, n)
    if i in hashmap[code]:
        continue
    else:
        hashmap[code].append(i)
for i in input_array:
    del_t = []
    for j in target:
        if j == 2 * i:
            continue
        temp = hash_func(j - i, n)
        if (j - i) in hashmap[temp]:
            del_t.insert(0, j)
    for j in del_t:
        target.pop(j)
        
        

