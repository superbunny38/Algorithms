import heapq

def find_middle(heap):
    if len(heap)%2 == 0:
        idx = len(heap)/2-1
        idx = int(idx)
        for _ in range(idx+1):
            kth_min = heapq.heappop(heap)
        return kth_min
    else:
        idx = len(heap)-1
        idx = idx/2
        idx = int(idx)
        for _ in range(idx+1):
            kth_min = heapq.heappop(heap)
        return kth_min
    
number_list = []
N = int(input())
for i in range(N):
    number = int(input())
    number_list.append(number)

for j in range(N):
    heap = []
    tmp_list = number_list[:j+1]
    for n in tmp_list:
        heapq.heappush(heap,n)
    print(find_middle(heap))
