#DP
def solve_dp(milk_list):
    N = len(milk_list)
    memoization = [[x for x in range(3)] for _ in range(N)]
    start_idx = milk_list.index(0)#strawberry마셔야 시작 가능
    memoization[start_idx][0] = 1
    need_to_drink = 1
    for store_idx in range(start_idx+1,N):
        current_milk = milk_list[store_idx]
        memoization[store_idx] = memoization[store_idx-1].copy()
        if current_milk == need_to_drink:
            memoization[store_idx][current_milk] = max(memoization[store_idx-1][(current_milk-1)%3]+1,memoization[store_idx-1][current_milk])
            #print(f"store: {store_idx} milk: {current_milk}: drink")
            need_to_drink = (current_milk+1)%3
            
            
    return max(memoization[-1])

N = int(input())#가게의 수
store_info = input().split()
store_info = [int(s) for s in store_info]
print(solve_dp(store_info))
