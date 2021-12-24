
def solution(number, k):
    answer = ''
    max_order = list(number)
    max_order.sort(reverse=True)#큰순서로저장
    n_array = list(number)#숫자하나씩저장
    tuple(n_array)
    answer_list = []#답
    i = 0
    jarisu = len(n_array) - k
    print("n_array:",n_array)
    print("max_array:",max_order)
    print("answer_Array:",answer_list)
    maxi =max_order[i]
        
    print("i:",i)
    print("maxi:",maxi)
        
    maxi_index = n_array.index(maxi)
    if len(n_array) - n_array.index(maxi) >= jarisu:#가능
        print(maxi,"append")
        answer_list.append(maxi)
        n_array = n_array[maxi_index+1:]#숫자 순서대로 유지
        jarisu = jarisu - 1#채워야하는 자리수 줄어듦
        i = i + 1
    else:
        print(maxi,"append 불가능!")
        i = i + 1#다음 큰 수
        maxi = max_order[i]

    if len(max_order) - k == len(answer_list):#자리수 다 채
        break
        
    answer = "".join(answer_list)#문자열로 문자들 합침
    return answer
    
print("ans",solution("1924",2))#94
print("\n\nEx2")
print("ans",solution("1231234",3))#3234
print("\n\nEx3")
print("ans",solution("4177252841",4))#775841
