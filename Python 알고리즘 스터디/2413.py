#2413
#비슷한 순열
#류채은

#input
n = int(input())#순열의 요소 개수
sunyeol = map(int,input().split())#8,5,7,3,6,4,2,1
sunyeol = list(sunyeol)

#8 -> 7, 8
#n이 8이라고 치면
# [7,8] -> [0]

#함수
def remove_n_in_array(n, array):
    
    for i in range(len(array)):
        if len(array[i]) == 1:
            if array[i][0] == 0:
                array[i] = [0]#possible리스트에서 정답이 발견되면 0으로 초기화
        else:
            if n in array[i]:
                array[i].remove(n)
        

#필요한 list들
possible = []
answer = [0]*n#답 저장하는 공간

for i in range(len(sunyeol)):#순열 처음부터 possible에 저장
    cur = sunyeol[i]
    cur_index = i
    tmp = []#7
    if cur - 1 > 0 :
        less = cur -1
        tmp.append(less)

        
    tmp.append(cur)
    if cur + 1 <= n:
        more = cur + 1
        tmp.append(more)
        
    possible.append(tmp)#[6,7,8]



first = sunyeol[0]#8
#print("순열의 첫번째:",first)
answer[0] = possible[0][0]#8의 가능성 요소들 가장 작은 것 [7,8]
#print("정답의 첫번째:",answer[0])

remove_n_in_array(answer[0], possible)
#print("정답의 첫 숫자 채운 후 possible: ",possible)
possible[0] = [0]
#print("8있음?:",possible)
#print(len(possible[8]),possible[8],possible[8][0])

idx = 1
cur_idx = 0
for k in range(n):
    if 0 not in answer:
        break
    print("cur_idx:",cur_idx)
    is_count = 0
    #print("answer:",answer)
    #count 1찾기
    for i in range(len(possible)):
        if len(possible[i]) == 1:#count가 1이면
            if possible[i][0] != 0:
                answer[i] = possible[i][0]
                print("answer넣음1:",possible[i][0])
                remove_n_in_array(possible[i][0],possible)
                possible[i] = [0]
                is_count = 1
                
                
    if is_count == 0:#count 1이 없으면 possible에서 가장 작은 값 정답으로 저장하는 코드
        cur_idx = cur_idx + 1
        if possible[cur_idx][0] != 0:
            answer[cur_idx] = possible[cur_idx][0]
            print("answer넣음2:",possible[cur_idx][0])
            remove_n_in_array(possible[cur_idx][0],possible)
            possible[cur_idx] = []
    cur_idx = cur_idx + 1  #다음 값의 답을 저장하기 위해 커서를 옮기는 것 answer[0] -> answer[1]

    #if cur_idx == n:
     #   cur_idx = 0
        
#print(answer) 
for value in answer:
    print(value,end=" ")
