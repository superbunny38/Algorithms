#11047
#동전 0
#류채은

N, K = map(int, input().split())#N, K 입력
value_list = []#가치 종류 담긴 리스트 선언

for i in range(N):#value_list에 값들 저장
    value = int(input())
    value_list.append(value)

value_list.sort(reverse = True)#내림차순으로 정렬

remnants = K #몫들을 뺀 나머지
count= 0#동전개수
for j in range(len(value_list)):
    divisor = value_list[j]#remnants를 나눌 가치
    if remnants >= divisor:
        #print(remnants,'를',divisor,'로 나누겠습니다.')
        dividend = remnants //divisor #몫
        #print('몫:',dividend)
        remnants = remnants - dividend * divisor
        count = count + dividend

    

#print(value_list)
print(count)
