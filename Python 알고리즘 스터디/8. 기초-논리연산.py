#8 기초-논리연산

'''
#53 **
#1(true) 또는 0(거짓)이 입력되었을 때 반대로 출력하는 프로그램을 작성해보자.

boolean = int(input())
print(not boolean)


#54***
#파이썬에서는 AND연산값이 참이면 뒤에 있는 값을 출력하게 된다.

for _ in range(4):
    a,b = map(int, input().split())
    print(a and b)


#55 ***
#파이썬에서는 OR연산값이 참이면 참인 값을 출력하게 된다.

for i in range(4):
    a, b = map(int, input().split())
    print(a or b)



#bonus
number = int(input())
print(number %2 and '홀수' or '짝수')


#56**** XOR 서로 다를 때 참

for _ in range(4):
    a, b = map(int, input().split())
    print(((a and (not b)) or ((not a) and b)))


'''
#57 *** 서로 같을 때 참

for _ in range(4):
    a, b = map(int, input().split())
    print((a and b) or( (not a) and (not b)))
    


#58 *** 모두 거짓일 떄만 참
for _in range(4):
    a, b = map(int, input().split())
    print(not (a or b))

























