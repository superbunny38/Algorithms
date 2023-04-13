
def exoj_print_mat(matrix):
    for arr in matrix:
        for idx,val in enumerate(arr):
            if idx != len(arr)-1:
                print(f" {val}",end = "")
            else:
                print(f" {val}")

            

def get_embed_list(N,M,cur_sum):
    if cur_sum == 0:
        return [[0,0]]
    else:
        candidates = []
        for row in range(cur_sum+1):
            column = cur_sum - row
            if row >= N or column >= M:
                continue
            candidates.append([row,column])
        return candidates

N, M = map(int, input().split())
embed = 1
n_count = N*M
mat = [[0 for _ in range(M)] for r in range(N)]
#print(mat)
cur_sum = 0

embed_dict = dict()
while True:
    if embed > n_count:
        break
    ret = get_embed_list(N,M,cur_sum)
    cur_sum +=1
    
    for emb in ret:
        embed_dict[tuple(emb)] = embed
        embed+=1
        
for key,val in embed_dict.items():
    y,x = key[0],key[1]
    mat[y][x] = val    
exoj_print_mat(mat)
