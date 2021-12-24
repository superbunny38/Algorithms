#2529
#부등호
#류채은
k = int(input())
signs = list(input().split())

max_numbers = []#9~가능범위
min_numbers = []#0~가능범위
for i in range(k + 1):
    min_numbers.append(i)
    max_numbers.append(9-i)
min_ans = [0]*(k+1)#0으로 초기화
max_ans = [0]*(k+1)
i = 0
p = 0
#최소
for i in range(k):
    conse = 0#>이 연속된 개수
    if signs[i] == '>':
        j = i
        while j < k:
            if signs[j] == '>':
                conse = conse + 1
            elif signs[j] == '<':
                break
            j = j + 1
        min_ans[p] = min_numbers[0] + conse
        min_numbers.remove(min_ans[p])#이미 썼기에 가능성에서 없앰
        
        
    elif signs[i] == '<':
        min_ans[p] = min_numbers[0]
        #print(p,'번째',min_ans[p])
        min_numbers.remove(min_ans[p])
        
    i = i + 1
    p = p + 1
    if i == k+1 and p == k+1:
        break
min_ans[k] = min_numbers[0]
               
#최대
i = 0
j = 0
p = 0
for i in range(k):
    conse = 0#>이 연속된 개수
    if signs[i] == '<':
        j = i
        while j < k:
            if signs[j] == '<':
                conse = conse + 1
            elif signs[j] == '>':
                break
            j = j + 1
        max_ans[p] = max_numbers[0] - conse
        max_numbers.remove(max_ans[p])#이미 썼기에 가능성에서 없앰
        
        
    elif signs[i] == '>':
        max_ans[p] = max_numbers[0]
        #print(p,'번째',min_ans[p])
        max_numbers.remove(max_ans[p])
        
    i = i + 1
    p = p + 1
    if i == k+1 and p == k+1:
        break
max_ans[k] = max_numbers[0]

#최대출력
print("".join(map(str,max_ans)))
#최소 출력
print("".join(map(str,min_ans)))
