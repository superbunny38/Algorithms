#20440
#Chaeeun Ryu
from collections import Counter
N = int(input())
flatten_ = []

for _ in range(N):
    enter_t,exit_t = map(int, input().split())
    for num in range(enter_t, exit_t, 1):
        flatten_.append(num)
data = Counter(flatten_)
highest_freq = data.most_common()[0]#time, frequency
time_range = []
frequency = highest_freq[1]
for tup in data.most_common():
    if tup[1] == frequency:
        time_range.append(tup[0])
print(frequency)
print(time_range[0],time_range[-1]+1)
        
