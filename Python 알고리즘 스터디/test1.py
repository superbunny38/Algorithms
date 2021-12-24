#류채은
#1
'''
a, b = map(int, input().split())
print(a,b)

#2
y, m, d = input().split('.')
if len(m) == 1:
    m = '0' + m
if len(d) == 1:
    d  = '0' + d

print('{}.{}.{}'.format(y,m,d))

#3
y, m, d = input().split('.')
if len(m) == 1:
    m = '0' + m
if len(d) == 1:
    d  = '0' + d

print('{}.{}.{}'.format(y,m,d))

#4 75253
five = int(input())

f1 = five // 10000
print("[{}]".format(f1*10000))
f2 = five // 1000 - f1 * 10
print("[{}]".format(f2*1000))
f3 = five // 100 - f1 * 100 - f2 * 10
print("[{}]".format(f3*100))
f4 = five // 10 - f1 * 1000 - f2 * 100 - f3 * 10
print("[{}]".format(f4*10))
f5 = five % 10
print("[{}]".format(f5))


#5
y, m, d = input().split('.')
if len(m) == 1:
    m = '0' + m
if len(d) == 1:
    d  = '0' + d

print('{}.{}.{}'.format(y,m,d))

#6
n1, n2 = map(int, input().split())

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 // n2)
print(n1 % n2)
print( round(n1 / n2,2))
'''
a = input()
b = len(a) - 1
for i in range(len(a)):
    
    print(str(a)[i] + ("0" * b))
    b -= 1
