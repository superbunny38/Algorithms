#프로그래머스
#조이스틱
#류채은
def solution(name):
    answer = 0
    mv=0 
    na=0 
    idx=0 
    first_a=0 
    a_max=0 
    
    for index, name in enumerate(name):
        if name == 'A': 
            na = na + 1
            if na > a_max:
                a_max = na
                idx = index
        else:
            answer = answer + min(ord(name)-ord('A'), ord('Z')-ord(name)+1)
            na = 0
    
    first_a = idx-a_max + 1
    
    if first_a == 0 or idx == len(name) -1:
        answer = answer + len(name)-1-a_max
        
    else:
        remainder = len(name)-idx-1 
        if first_a <= remainder:
            mv = (first_a-1)*2 + remainder
        else:
            mv = (first_a-1) + remainder*2

        answer = answer + min(mv, len(name)-1) 
    return answer
