#DP
#2775

def fill(memoization,floor_n,room_num):
    memoization[floor_n][room_num] = sum(memoization[floor_n-1][:room_num+1])
        

def do_dp(memoization,max_floor,max_roomnumber):
    for floor_n in range(1,max_floor+1):#1층부터 채우기 시작, 0층은 이미 완료
        for room_num in range(max_roomnumber):
            fill(memoization,floor_n,room_num)

def get_dp(memoization,get):
    for item in get:
        floor,roomn = item[0],item[1]
        print(memoization[floor][roomn-1])


T = int(input())#test cases
memoization = [[0 for _ in range(14)] for f in range(15)]
get = []

for ins in range(1,15):
    memoization[0][ins-1] = ins

max_floor = 0
max_roomnumber = 0

for _ in range(T):
    need = []
    for tmp in range(2):
        need.append(int(input()))
    k, n = need[0],need[1]
    if k > max_floor:
        max_floor = k
    if n > max_roomnumber:
        max_roomnumber = n
    get.append((k,n))#층, 호

#print("max floor:",max_floor,"max room number:",max_roomnumber)
do_dp(memoization,max_floor,max_roomnumber)
get_dp(memoization,get)
#print("memoization:")
#for m in memoization[::-1]:
#    print(m)
                                             
