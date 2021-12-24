#프로그래머스
#큰 수 만들기
#류채은


def solution(number, k):
    answer = ''
    answer_list = []#답 숫자 하나씩 저장한 배열
    n_array = list(number)#숫자 하나씩 저장한 배열
    tuple(n_array)
    jarisu = len(n_array) - k#반환 값 자리수
    i = 0
    max_order = list(number)
    max_order.sort(reverse = True)#큰 순서대로 저장
    maxi = max_order[0]#가능한 가장 큰 수(아직 가능한지 파악x)
    
    while True:
        i = i + 1
        print("max order:",max_order)
        
        #가능성 파악
        print("n_array",n_array)
        
            maxi_index = n_array.index(maxi)
            if len(n_array) - n_array.index(maxi) < jarisu:#불가능
                
                maxi = max_order[i]#다음으로 큰 것
            else:#가능
                print(maxi,"가능")
                answer_list.append(maxi)#답에 추가
                jarisu = jarisu -1#채워야 하는 자리수 줄어듦
                print(jarisu,'만큼 채워야함')
                n_array = n_array[maxi_index+1:len(n_array)]#숫자 순서대로 유지하기 위해 maxi index 앞의 것 잘라낸 것
                

        
            print(maxi,"maxi 없음")
            #없으면 다음 큰 것 찾
            maxi = max_order[i]
            

        if len(answer_list) == len(max_order)-k:#자리수 다 채웠으면 반복문 탈출
            break
    answer = "".join(answer_list)#문자열로 문자들 합침
    return answer


print("ans",solution("1924",2))#94

print("ans",solution("1231234",3))#3234
print("ans",solution("4177252841",4))#775841
