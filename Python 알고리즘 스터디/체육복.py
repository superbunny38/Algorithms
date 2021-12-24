#프로그래머스
#류채은

#lost 기준

def solution(n, lost, reserve):
    answer = 0
    saved_count = 0
    tmp_lost = lost
    saved = []
    for value in lost:
        #print("got:",value)
        for i in range(len(reserve)):
            if abs(value - reserve[i]) == 1:
                #print(value,"can be saved by", reserve[i])
                saved.append([value,reserve[i]])
    #print(saved)
    i = 1
    if len(saved) > 2:
        saved_count = 1
        while i < len(saved):
            prev = saved[i-1]
            if saved[i-1][0] != saved[i][0]:
                if saved[i][1] != saved[i+1][1]:
                    #print("!!",saved[i])
                    saved_count = saved_count + 1
            i = i + 1
        answer = n - (len(lost) - saved_count)
    else:
        if len(saved) == 2:
            if saved[0][0] == saved[1][0] or saved[0][1] == saved[1][1]:
                saved_count = 1
            else:
                saved_count = 2
            answer = n - (len(lost) - saved_count)
        else:
            saved_count = len(saved)
            answer = n - (len(lost) - saved_count)
    return answer

n = 5
lost = [2,4]
reserve=[1,3,5]
print(solution(n,lost,reserve))
