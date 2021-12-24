#2785
#류채은
#체인
'''
5
4 3 5 7 9
'''
N = int(input())
L = list(map(int,input().split()))

L.sort()

i = 0
interval = N-1
final_n_links = 0

while True:
    links = L[i]
    interval -= 1
    #print("\nlinks:",links)
    #print("interval:",interval)
    if interval > links:
        #print("first")
        final_n_links += links
        interval -= links
        if interval == 1:
            final_n_links += 1
            break
    elif interval < links:
        #print("second")
        
        interval += 1
        links = interval
        final_n_links += links
        break
    else:
        #print("third")
        #print("same")
        final_n_links += links
        break
    i = i + 1
    #print("i=i+1")
    
print(final_n_links)
