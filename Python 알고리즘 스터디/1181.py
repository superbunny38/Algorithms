#1181
#단어 정렬
'''
def Insert(age, name, member):
        member[name] = age
        return member
        

member = dict()
n = int(input())
for i in range(n):
    a, name = input().split()
    age = int(a)
    member = Insert(age, name, member)
    
import operator
sorted_d = dict(sorted(member.items(), key=operator.itemgetter(1)))
 
for key, value in sorted_d.items():
    print("{} {}".format(value, key))

####



words = dict()


n = int(input())
for i in range(n):
    word = input()
    length = len(word)
    alphabet = ord(word[0])
    words = Insert(word, length, alphabet, words)

import operator
sorted = dict(sorted(member.items(), key=operator.itemgetter(1)))
'''
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if ord(arr[j][0]) < ord(arr[j+1][0]):
                arr[j],arr[j+1] = arr[j+1],arr[j]



alphabet = []
n = int(input())
words = [[0 for x in  range(n)] for y in range(n)]
for i in range(n):
    word = input()
    length = len(word)
    alphabet = ord(word[0])
    words[length].append(word)

for j in range(len(words)):
    if len(words[j])>1:
        for a in words[j]:
            alphabet.append(a)
        bubbleSort(alphabet)
        for i in alphabet:
            print(i)
        alphabet.clear()
    else:
        print(words[j])        
        
        


    





















'''

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        

n = int(input())
words = []
length_sorted = []
lengthly = []

final = []
for _ in range(n):
    word = input()
    words.append(word)
    length_sorted.append(len(word))

bubbleSort(length_sorted)

for i in range(n):
    for j in range(len(length_sorted)):
        if len(words[i]) == length_sorted[j]:
            lengthly.append(words[i])


'''

    


    
