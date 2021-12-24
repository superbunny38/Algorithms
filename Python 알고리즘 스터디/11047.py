#11407
#류채은

N, M = map(int,(input().split()))
value = []
count = 0
for i in range(N):
    tmp = int(input())
    value.append(tmp)

print(value)

for k in range(N):
    division =  M // value[N-k-1]
    print('value: ',value[N-k-1], 'division: ',division)
    if division > 0:
        M = M - value[N-k-1]*division
        #print('divided by',value[N-k-1],'for',division,'times')
        count = count + division
print(count)
