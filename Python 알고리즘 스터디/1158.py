#1158
#요세푸스 문제
#류채은

# 1 2 3 4 5 6 7
# 1 2V 3V 4 5 6V 7
# 3
n, k = map(int,input().split())
people = []
for i in range(n):
    people.append(i+1)

cur = k - 1
answer = []
for _ in range(n):    
    tmp = people[cur]
    answer.append(tmp)
    #print(">>>>>>>",tmp)
    people.remove(tmp)
    #print("ppl:",people)
    for _ in range(k-1):
        if cur == len(people):
            #print("0으로")
            cur = 0
        elif cur == len(people)-1:
            cur = -1
            
        cur = cur + 1
    #print("cur:",cur)
for value in answer:
    print(value, end = ' ')

