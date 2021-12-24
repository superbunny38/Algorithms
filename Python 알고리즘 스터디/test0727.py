#test0727
#류채은
#71 #?????
num = list(map(int, input().split()))

def a (num, n) :
    
    if num[n] == 0 :
        return
    print(num[n])
    n += 1
    a(num,n)

a(num, 0)



#71-1

def goto(array, i):
    if array[i] == 0:
        return
    print(array[i])
    i += 1
    goto(array, i)

array = list(map(int, input().split()))
goto(array, i = 0)


#63-2
a,b = map(int, input().split())
print(a>b and a or b)

#65

a,b,c = map(int, input().split())
if a%2 == 0:
    print(a, end = ' ')
if b%2 == 0:
    print(b, end = ' ')
if c%2 == 0:
    print(c, end = ' ')

#66

a,b,c = map(int, input().split())
if a%2 == 0:
    print("even", end = ' ')
else:
    print("odd", end= ' ')
if b%2 == 0:
    print("even", end = ' ')
else:
    print("odd", end= ' ')
if c%2 == 0:
    print("even", end = ' ')
else:
    print("odd", end= ' ')

#65
a,b,c = map(int, input().split())
if a%2 == 0:
    print(a, end = ' ')
if b%2 == 0:
    print(b, end = ' ')
if c%2 == 0:
    print(c, end = ' ')


#72
def goto(a, n, i):
    if n == i:
        return
    print(a[i])
    i = i + 1
    goto(a,n,i)

n = int(input())
a = list(map(int, input().split()))
goto(a,n,i=0)

#67
n = int(input())
if n <0:
    print("minus")
else:
    print("plus")
if n%2==0:
    print("even")
else:
    print("odd")

#73

array = list(map(int, input().split()))
for a in array:
    if a == 0:
        break
    print(a)


#68
score = int(input())
if 90<=score<=100:
    print('A')
elif 70<=score<90:
    print('B')
elif 40<=socore<70:
    print('C')
else:
    print('D')
  

#69
score = input()
if score == 'A':
    print('best!!!')
elif score == 'B':
    print('good!!')
elif score == 'C':
    print('run!')
elif score == 'D':
    print('slowly~')
else:
    print('what?')


    
