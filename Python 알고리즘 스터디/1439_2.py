#1493
#뒤집기
#류채은
array = list(input())#input 숫자열

seq = []#count continuos 0 or 1

prev = array[0]
seq.append(prev)
for i in range(len(array)):
    if prev != array[i]:#전과 현재가 다르면
        seq.append(array[i])
    prev = array[i]
n_one = 0
n_zero = 0

for j in range(len(seq)):#seq에서 0과 1을 각각 센 다음 적은 걸 출력
    if seq[j] == '0':
        n_zero = n_zero + 1
    elif seq[j] == '1':
        n_one = n_one + 1

if n_one > n_zero:
    print(n_zero)
else:
    print(n_one)
    

            
