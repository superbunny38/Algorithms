#1439
#류채은

def n_conse(S):
    if S[0] == '1':
        #print('1부터 시작하는 S')
        n_one = 1#1의 연속적 수열 개수
        n_zero = 0#0의 연속적 수열 개수
        prev = '1'
        for i in range(len(S)):
            if S[i] != prev:
                if prev == '1':
                    if n_one != 1:
                            
                        print('인덱스',i,'에서 바뀜')
                        n_one = n_one + 1
                        prev = '0'
                elif prev == '0':
                    print('인덱스',i,'에서 바뀜')
                    n_zero = n_zero + 1
                    prev = '1'
        print('n_one',n_one)
        print('n_zero',n_zero)
        if n_one > n_zero and n_zero != 0:
            return n_zero
        elif n_zero == 0 and n_one == 1:
            return n_one
                
    elif S[0] == '0':
        #print('0부터 시작하는 S')
        n_one = 0
        n_zero = 1
        prev = '0'
        for i in range(len(S)):
            if S[i] != prev:
                if prev == '1':
                    if n_zero != 1:
                        print('인덱스',i,'에서 바뀜')
                        n_one = n_one + 1
                        prev = '0'
                elif prev == '0':
                    print('인덱스',i,'에서 바뀜')
                    n_zero = n_zero + 1
                    prev = '1'
        print('n_one',n_one)
        print('n_zero',n_zero)
        if n_zero > n_one and n_one != 0:
            return n_zero
        elif n_one == 0 and n_zero == 1:
            return n_one
        
    #print('n_one',n_one)
    #print('n_zero',n_zero)
    
S = list(input())

print(n_conse(S))
