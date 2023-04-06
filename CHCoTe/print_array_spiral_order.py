
def exoj_print(arr1d):
    for idx, value in enumerate(arr1d):
        if idx == len(arr1d)-1:
            print(f" {value}")
        else:
            print(f" {value}",end = "")

def print_spiral(arr,start_y,start_x,cur_access):
    #오른 아래 왼 위
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    H,W = len(arr),len(arr[0])
    if H == 1 or W == 1:
        n_access = H*W
    else:
        n_access = (W-2*start_x)+W-2*start_x+(H-2-2*start_y)+(H-2-2*start_y)
    tmp_cur_access = 0
    cur_y,cur_x = start_y,start_x
    #print("n need to access:",n_access)
    if n_access <0:
        return
    try:
        arr[start_y][start_x]
        if arr[start_y][start_x] != 0:
            return
    except:
        return
    arr[start_y][start_x] = cur_access+1
    cur_access +=1
    tmp_cur_access+=1
    for move_y, move_x in zip(dy,dx):
        while 0<=cur_y+move_y <H and 0<= cur_x+move_x<W:
            if tmp_cur_access>n_access:
                break
            
            if arr[cur_y+move_y][cur_x+move_x] == 0:
                cur_y,cur_x = move_y+cur_y,move_x+cur_x
                cur_access +=1
                tmp_cur_access+=1
                #print(f"cur: ({cur_y},{cur_x})")
                arr[cur_y][cur_x] = cur_access
            else:
                break
            
            
        else:
            continue

    #print(f"({start_y},{start_x})",arr)
    
    print_spiral(arr,start_y+1,start_x+1,cur_access)
    

N,M = map(int,input().split())
mat = [[0 for _ in range(M)] for r in range(N)]
#print("init:",mat)
print_spiral(mat,0,0,0)
for m in mat:
    exoj_print(m)
