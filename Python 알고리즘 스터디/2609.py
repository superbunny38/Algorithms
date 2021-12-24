#2609 류채은
from math import gcd
a,b = map(int, input().split())
'''

def sosu(n):
    for i in range(n):
        if i!= 1 and i!= 0:
            if n % i == 0:
                return False
    return True

#최대 공약수
yaksu_a = []
yaksu_b = []
i = 1
j = 1

while i<= a:
    if i!=1 and i != 0:
        if a % i == 0:
            if sosu(i) == True:
                #print('append',i)
                yaksu_a.append(i)
    i = i + 1


while j <= b:
    if j!=1 and j != 0:
        if b % j == 0:
            if sosu(j) == True:
                #print('append',j)
                yaksu_a.append(j)

    j = j + 1

yaksu = yaksu_a + yaksu_b
yaksu = list(set(yaksu))
#print('yaksu:',yaksu)
result = 1
for value in yaksu:
    result = value * result

print(result)
'''
def gcd(x,y):
    while y:
        x,y = y, x%y
    return x
print(gcd(a,b))

def lcm(x,y):
    return x*y//gcd(x,y)
print(lcm(a,b))

'''
#최소 공배수
baesu_a = []
baesu_b = []
baesu = baesu_b + baesu
i = 2
while i <= a:
        if sosu(i) == True:
            while a % i == 0:
                baesu_a.append(i)
                a = a // i
        i = i + 1
print('ba',baesu_a)
j = 2
while j < b:
        if sosu(j) == True:
            while b % j == 0:
                baesu_b.append(j)
                b = b // j
        j = j + 1
print('bb',baesu_b)
    
for value in baesu_a:
    if value not in baesu_b:
        baesu.append(value)
result2 = 1
for value in baesu:
    result2 = value * result2

print(result2)
'''
