#12 기초-반복실행구조
'''
#71

a = input().split()
for x in a:
    if int(x) == 0:
        break
    else:
        print(x)

def goto(array, i):
    if array[i] == 0:
        return
    print(array[i])
    i += 1
    goto(array, i)

array = list(map(int, input().split()))
goto(array, i = 0)

#72**?
nlist = []
n = int(input())
number = input().split()
for x in number:
    nlist.append(int(x))
n

for i in range(n):
    print(nlist[i])
    i = i + 1
'''
'''
n = int(input())
number = list(map(int, input().split()))

def goto(number, n, i):
    if i == n: return
    print(number[i])
    i += 1
    goto(numeber,n,i)

goto(number, n, 0)


#73**
number = map(int, input().split())
for element in number:
    if element is not 0:
        print(element)
        continue
    break
numbers = map(int, input().split())
for value in numbers:
    if value ==0:
        break
    print(value)

#74**

n = int(input())
for i in range(n,0,-1):
    print(i)
for i in range(n):
    print(n-i)
    i = i + 1

#75#C언어for문이랑비슷한듯

count = int(input())
for i in range(count-1, -1, -1):
    print(i)

    


#76 **
converter = ord(input())
#print(converter)
for i in range(97, converter+1):
    print(chr(i), end=' ')


#77**
count = int(input())
i = 0
while count >= 0:
    print(i)
    i += 1
    count -= 1

number = int(input())
for i in range(0,number+1):
    print(i)
    '''






