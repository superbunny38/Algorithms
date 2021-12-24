#프로그래머스
#큰 수 만들기

def solution(number, k):
    answer = ''
    #가능한 가장 큰 수 찾아나섬
    n_array = list(number)
    max_order = list(number)
    max_order.sort(reverse=True)
    print(max_order)
    maxi = max_order[0]#가능한 가장 큰 수(아직 가능한지 여부 파악x)
    jarisu = len(n_array) - k#반환할 숫자의 자리수
    i = 1
    while i < len(n_array):
        if len(n_array) - n_array.index(maxi) < jarisu:#불가능 (같으면..?
            maxi = max_order[i]
        else:#가능
            break
        i = i+ 1
    j = n_array.index(maxi)
    new_array = []#max index부터 n_array 끝까지 끌고올 새로운 리스트
    min_array = []#작은 순서로 정렬할 리스트
    while j < len(n_array):
        new_array.append(n_array[j])
        min_array.append(n_array[j])
        j = j + 1
    n_discard = len(new_array) - jarisu#새로운 리스트에서 버릴 개수
    min_array.sort()
    for k in range(n_discard):
        new_array.remove(min_array[k])#작은 순서로 n_discard개수 만큼 없
    
    answer = "".join(new_array)#문자열로 문자들 합침
    return answer

print(solution("1924",2))#94

print(solution("1231234",3))
print(solution("4177252841",4))

