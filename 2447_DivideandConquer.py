def fill(start_row_idx, start_col_idx,matrix,N):
    count_blocks = (N/3)*(N/3)#number of blocks to fill
    #print("start row:{} start col:{}, N: {}".format(start_row_idx, start_col_idx,N))
    for i in range(int(N/3)):
        for j in range(int(N/3)):
            #print("fill matrix[{}][{}]".format(start_row_idx+int(N/3)+i, start_col_idx+int(N/3)+j))
            matrix[start_row_idx+i+int(N/3)][start_col_idx+j+int(N/3)] = " "
    return matrix

def fill_part_matrix(matrix,N):
    #print("designing {}x{} initiated".format(N,N))
    repeat = int(len(matrix)/N)
    #print("fill {} partial matrices".format(repeat))
    for u in range(repeat):#repeat
        row_idx = u*N
        for v in range(repeat):#repeat:
            col_idx = v*N
            #print("row:{},col:{}".format(row_idx,col_idx))
            matrix = fill(row_idx,col_idx,matrix,N)
            #print("\n")
    return matrix

def display_matrix(matrix):
    for m in matrix:
        print("".join(m))

def fill_matrix(matrix, N):
    k = N**(1/3)
    i = 1
    while i<=k:
        tmp_N = 3**i
        matrix = fill_part_matrix(matrix,tmp_N)
        i+=1
    return matrix

#input
N = int(input())
assert N%3 == 0
assert N>0
#initialize matrix
matrix = [ [ '*' for i in range(N) ] for j in range(N) ]
matrix = fill_matrix(matrix,N)
display_matrix(matrix)


