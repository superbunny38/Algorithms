def ATM(N, nums):
    
    # return : min_sum # 인출 시간 합의 최소값
    
    ########### 함수 완성하기 ##########
    
    # 사람이 1명인 경우
    if N == 1:
        min_sum = nums[0]

    
    
    # 사람이 2명 이상인 경우
    # bubble sort 사용
    elif N>1:
        
        idx_time = dict()
        
        for idx, ti in enumerate(nums):
            idx = 'person'+str(idx)
            idx_time[idx] = ti
            
        #print(idx_time)
        #bubble_sort
        n = len(nums)
        for i in range(n-1):#sort time
            for j in range(0,n-i-1):
                #swap
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1],nums[j]
        min_sum = 0
        for k in range(len(nums)):
            min_sum += sum(nums[:k+1])

    
    
    
    
    
    
    
    
    
    
    
    

    #####################################
    return min_sum

### do not edit here ###
print('최소 시간:', ATM(5, [3, 1, 4, 3, 2]))
