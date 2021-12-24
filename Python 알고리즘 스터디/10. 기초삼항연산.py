#10 기초-삼항연산
'''
#63**
a, b = map(int, input().split())
print(a>b and a or b)

#64**
a,b,c = map(int, input().split())
num = a if a<b else b
print(num if num <c else c)
'''
#bonus**
number = int(input())
print('홀수' if number%2 else '짝수')

'''
a,b,c = map(int, input().split())
if a<b:
    num = a
else:
    num = b

if num<c:
    print(num)
else:
    print(c)
    
'''
