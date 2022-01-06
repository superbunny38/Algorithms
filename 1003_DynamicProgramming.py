

zeros = [1,0]
ones = [0,1]
t = int(input())
n_list = []
for _ in range(t):
    tmp_n = int(input())
    n_list.append(tmp_n)

max_n = max(n_list)
if max_n>len(zeros):
    for _ in range(max_n-len(zeros)+1):
        zeros.append(0)
        ones.append(0)
idx = 2
#print(max_n+1-2)
for _ in range(max_n+1-2):
    zeros[idx] = zeros[idx-1]+zeros[idx-2]
    ones[idx] = ones[idx-1]+ones[idx-2]
    idx += 1
#print(zeros)
#print(ones)

for n in n_list:
    print("{} {}".format(zeros[n],ones[n]))

    
