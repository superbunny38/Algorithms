#array-handling
#->
#<-
def exoj_print(arr):
    for idx, num in enumerate(arr):
        if idx == len(arr)-1:
            print(f" {num}")
        else:
            print(f" {num}", end = "")

def print_style1(arr):
    for idx,row_arr in enumerate(arr):
        if idx%2 == 0:
            exoj_print(row_arr)
        else:
            exoj_print(row_arr[::-1])

N = int(input())
mat = []
num = 1
for r in range(N):
    tmp_mat = []
    for c in range(N):
        tmp_mat.append(num)
        num+=1
    mat.append(tmp_mat)
print_style1(mat)
