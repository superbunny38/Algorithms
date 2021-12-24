#[2] 기초 - 입출력


#13

var = list(map(int, input().split()))
print(var[0], var[1])

#14

var2 = input().split()
print(var2[1],var2[0])

#15

var3 = round(float(input()),2)
print(var3)

#17

h, m = input().split(':')
print('{}:{}'.format(h,m))

#18
print('number',18)

y,m,d = input().split('.')
if len(m) == 1:
    m = '0'+m
if len(d) == 1:
    d = '0'+d

print('{}.{}.{}'.format(y,m,d))

#19
a,b = input().split('-')
print('{}{}'.format(a,b))
print(a+b)

#22

string = input()
print(string)



#23 실수 1개 입력 받아 정수부분 실수부분 구분

string = input().split('.')

print('''#\
#{}
#{}
'''.format(string[0],string[1]))
#a,b = input().split('.')
#print('{}'.format(a))
#print('{}'.format(b))


#24 **

word = input()
for i in range(len(word)):
    print("'{}'".format(word[i]))


#25

integer = input()
count = len(integer) - 1
for i in range(len(integer)):
    print([int(integer[i]+'0'*count)])
    count -= 1

#num = input()
#for i in range(len(num)):
#    print("'{}'".format(num[i]+'0'*(len(num)-i-1)))


#26
h,m,s = input().split(':')
print(m)
#print('{}'.format(m))




#27
y,m,d = input().split('.')
if len(m) == 1:
    m = '0'+m
if len(d) == 1:
    d = '0'+d
print('{}-{}-{}'.format(d,m,y))





































