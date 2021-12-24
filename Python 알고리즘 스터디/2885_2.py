#2885_2
#초콜릿 식사
#류채은

k = int(input())

divide = 0#쪼갠 개수

size = 1#초콜릿바 크기
while size < k:
    size = size * 2
    
final_size = size
#print(size)

while k != 0:
    if k >= size:
        k = k - size#먹을 수 있는 개수 비

    else:
        size = size/2#쪼갬
        divide = divide + 1


print(final_size, divide)
