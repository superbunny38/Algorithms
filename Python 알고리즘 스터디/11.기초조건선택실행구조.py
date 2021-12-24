#11 기초-조건/선택실행구조

'''
#65***
a,b,c = map(int, input().split())
if not a%2: print(a)
if not b%2: print(b)
if not c%2: print(c)

d,e,f = map(int, input().split())
print(*(filter(lambda num:num%2==0, [d,e,f])))


#66****

a,b,c = map(int,input().split())
print('odd' if a%2 else 'even')
print(b%2 and 'odd' or 'even')
print(['even','odd'][c%2])

d,e,f = map(int, input().split())
print(*map(lambda num: 'odd' if num%2 else 'even', [d,e,f]))


#67
num = int(input())
print(num>0 and 'plus' or 'minus')#true가 앞
print(num%2 and 'odd' or 'even')

number = int(input())
print('minus' if number<0 else 'plus')
print('odd' if number%2 else 'even')
'''

#70**
month = int(input())

if month in [12,1,2]:
    print('winter')
elif month in [3,4,5]:
    print('spring')
elif month in [6,7,8]:
    print('summer')
else:
    print('fall')






