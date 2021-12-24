#큰수만들기
#류채
def solution(number, k):
    answer = ''
    max_array = list(number)#큰 수대로 정렬
    max_array.sort(reverse=True)
    n_array = list(number)
    i = 0
    jarisu = len(n_array) - k
    answer_list = []#답
    #print("max_array:",max_array)
    while True:
        maxi = max_array[i]
        #print("n_array:",n_array)
        if maxi in n_array:#부분 리스트에 큰 수가 있는 경
            if len(n_array) - n_array.index(maxi) >= jarisu:#가능
                jarisu = jarisu - 1
                maxi_index = n_array.index(maxi)
                n_array = n_array[maxi_index+1:]
                answer_list.append(maxi)
                #print("append:",maxi)
                i = 0
            else:#불가능
                i = i + 1
        else:
            i = i + 1
        if len(max_array) - k == len(answer_list):
            break
    answer = "".join(answer_list)
    return answer
    
print(solution("1924",2))#94

print(solution("1231234",3))#3234

print(solution("4177252841",4))#775841
