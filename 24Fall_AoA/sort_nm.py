def sort_lists(lists, m):
    # Step 1: Initialize buckets for each number in range [1, m]
    buckets = [[] for _ in range(m+1)]  # Create m buckets (0-indexed)
    sorted_lists = [[] for _ in range(len(lists))]
    
    # count
    for list_idx, list_i in enumerate(lists):
        for element in list_i:
            buckets[element].append(list_idx)
    
    
    for idx in range(1,m+1):
        for list_idx in buckets[idx]:
            sorted_lists[list_idx].append(idx)
        

    return sorted_lists


lists = [[3,2,1,6,5],[5,8,4,1,3],[4,2,5,6]]
print(sort_lists(lists,8))
