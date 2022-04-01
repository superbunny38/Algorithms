import sys

def split(word):
    return [char for char in word]


def count_goods(N,numbers_list):
    answer = 0

    for i in range(N):
        
        dump = numbers_list[:i] + numbers_list[i+1:]
        first = 0
        last = len(dump) - 1

        standard = first < last
        
        while standard:
            total = dump[last] + dump[first]

            if total == numbers_list[i]:
                answer += 1
                break
            
            elif total < numbers_list[i]:
                first += 1
                
            else:
                last -= 1
            standard = first<last
            
    return answer

    
number = int(input())
numbers_list = input().split()
numbers_list = [int(x) for x in numbers_list]
numbers_list.sort()
#A.sorted()

print(count_goods(number,numbers_list))
