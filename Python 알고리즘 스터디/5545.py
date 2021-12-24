#5545
#최고의 피자
#류채은
import math
maximum = 0
N = int(input())
A, B = map(int, input().split())
C = int(input())
D = []
for q in range(N):
    tmp = int(input())
    D.append(tmp)

D.sort(reverse = True)#열량이 큰 순서대로 토핑 저장함
toppings = D
n_toppings = 0#토핑의 개수

for i in range(N):#토핑의 종류만큼 반복
    n_toppings = i
    total_price = A + B*n_toppings
    total_kcal = C
    for k in range(i):
        total_kcal += toppings[k]#열량 높은 토핑 순서대로 추가함
    result = total_kcal/total_price
    
    if result > maximum:#1원당 피자가 가장 열량이 클 때를 구함
        maximum = result

print(math.trunc(maximum))
