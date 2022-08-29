#프로그래머스
#문자열 압축
#Chaeeun Ryu

def solution(s):
    answer = 0
    def split_n(s,n):
        #print("n:",n)
        result_ = []
        start_idx = 0
        for _ in range(int(len(s)/n)):
            try:
                tmp_ = s[start_idx:n+start_idx]
                result_.append(tmp_)
                start_idx = start_idx + n
            except:
                continue
            
        if len(s)%n != 0:
            result_.append(s[start_idx:])
        return result_

    def compress(result):
        #print("received:",result)
        compressed_ = ""
        cur_count = 1
        for idx, r in enumerate(result):
            if idx == 0:
                prev = r
            else:
                if prev == r:
                    cur_count +=1
                    if idx == len(result)-1:
                        if cur_count != 1:
                            compressed_ += str(cur_count)
                        compressed_ += r
                else:
                    #문자열 저장
                    if cur_count != 1:
                        compressed_ += str(cur_count)
                    compressed_ += prev
                    cur_count = 1
                    prev = r
                    if idx == len(result)-1:
                        compressed_ += r
        return compressed_
    min_length = len(s)
    #print("length of string:",min_length)
    for i in range(len(s)-1):
        n_ = i+1
        if n_ < len(s)//2+1:
            
            result = split_n(s,n_)
            compressed = compress(result)
            #print("n:",n_)
            #print("compressed:",compressed)
            length = len(compressed)
            #print("length:",length)
            if length < min_length:
                min_length = length
    answer = min_length
    return answer

s="abcabcdede"
print(solution(s))
