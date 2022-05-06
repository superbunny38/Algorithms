##인풋받는 방법들 정리

#여러개 받을 때 sys.stdin.readline()
import sys

T = int(input()) #Test case
for i in range(T):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

#임의의 개수의 정수를 한 줄에 입력 받아 리스트에 저장
import sys
data = list(map(int,sys.stdin.readline().split()))



#문자열 n줄을 입력받아 리스트에 저
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]


#하나의 문자열
import sys

sentence = sys.stdin.readline()


######### input()이용

#리스트 받기
# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) # adding the element
     
print(lst)



#split
# Python3 program to Split string into characters
def split(word):
    return [char for char in word]


#join
print(' '.join(tmp_list))




###원소 제거

#remove
animals.remove('rabbit')

#pop
two = my_list.pop(-1)

#del
del my_list[:]  # 리스트 모두 삭제

del my_list[0]  # index 0 삭제
