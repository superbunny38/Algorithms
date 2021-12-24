#1120
#문자열
#류채은

def find_n_same(j, new_A, list_A, list_B):#같은 문자 개수 찾는 함수
    same = 0
    newnew = new_A
    k = len(list_A)-1
    
    while k >= 0:
        newnew.insert(j, list_A[k])
        k = k - 1
    for p in range(len(list_B)):
        if newnew[p] == list_B[p]:
            #print(list_B[p],"같음")
            same = same + 1
        if newnew[p] == '0':
            same = same + 1
    #print('same: ',same)
    return same
    
list_A, list_B = map(list, input().split())#알파벳으로 쪼개서 리스트에 입력

new_A = []#문자 추가할 새로운 A리스트

length_diff = len(list_B) - len(list_A)#문자열 길이 차이

for i in range(length_diff):#새로운 문자는 0처리
    new_A.append('0')  
max_s = 0
for j in range(len(new_A)+1):
    tmp = find_n_same(j, new_A, list_A, list_B)
    if max_s < tmp:
        max_s = tmp
    new_A.clear()
    for i in range(length_diff):
        new_A.append('0')
    
result = len(list_B) - max_s#B길이에서 같은 걸 뺌
print(result)
