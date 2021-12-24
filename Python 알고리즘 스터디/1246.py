#1246
#온라인 판매
#류채은
p = []#가격 리스트
n, m = map(int,input().split())#n 공급, m수요 입력
for i in range(m):#수요
    price = int(input())
    p.append(price)#가격들 순서대로 저장

p.sort()#작은 것부터 정렬

max_r = 0#최대수익

for j in range(m):
    if m-j < n:#수요 < 공급
        result = p[j] * (m-j)
    else:
        result = p[j] * n#사람 수 x 최소 가격

    if result > max_r:#최대값 < 결과
        max_r = result
        price = p[j]


print(price,max_r)
    
    
    
