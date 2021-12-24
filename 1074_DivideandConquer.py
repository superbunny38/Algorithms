import sys
def create_matrix(N):
    size = 2**N
    matrix = [ [ '□' for i in range(size) ] for j in range(size) ]
    return matrix

def display_matrix(matrix):
    for m in matrix:
        for item in m:
            print("%4s"%item,end="")
        
def fill_matrix(matrix,queue):
    for q in queue:
        start_row_idx = q[0]
        start_col_idx = q[1]
        matrix[start_row_idx, start_col_idx] = '■'
    return matrix
        
def display_queue(queue):
    for q in queue:
        print(q)
        
def number_z(matrix, n,start_row_idx,start_col_idx):
    start_row_idx = int(start_row_idx)
    start_col_idx = int(start_col_idx)
    matrix[start_row_idx][start_col_idx] = str(n)
    matrix[start_row_idx][start_col_idx+1] = str(n+1)
    matrix[start_row_idx+1][start_col_idx] = str(n+2)
    matrix[start_row_idx+1][start_col_idx+1] = str(n+3)
    return matrix
        
        

def partition_matrix(matrix):
    print("partitioning matrix...")
    queue = [[0,0,len(matrix)]]
    while queue[0][2] != 2:
        dequeued = queue.pop(0)
        half_point = dequeued[2]/2
        start_row_idx = dequeued[0]
        start_col_idx = dequeued[1]
        first_quarter = [start_row_idx,start_col_idx,half_point]
        second_quarter = [start_row_idx,start_col_idx+half_point,half_point]
        third_quarter = [start_row_idx+half_point,start_col_idx,half_point]
        fourth_quarter = [start_row_idx+half_point,start_col_idx+half_point,half_point]
        queue = queue + [first_quarter, second_quarter, third_quarter, fourth_quarter]
    
    return queue

def find_plane(dequeued, r,c):
    half_point = dequeued[2]/2
    start_row_idx = dequeued[0]
    start_col_idx = dequeued[1]
    if r<=start_row_idx+half_point-1 and c<=start_col_idx+half_point-1:
        return 1#1사분면
    elif r<=start_row_idx+half_point-1 and c>=start_col_idx+half_point-1:
        return 2
    elif r>=start_row_idx+half_point-1 and c<=start_col_idx+half_point-1:
        return 3
    else:
        return 4
    
def better_partition_matrix(len_matrix,r,c):
    #print("partitioning matrix...")
    queue = [[0,0,len_matrix]]#start_row,start_col,length of row
    
    plane_queues = []
    while queue[0][2] != 2:
        dequeued = queue.pop(0)
        
        half_point = dequeued[2]/2
        start_row_idx = dequeued[0]
        start_col_idx = dequeued[1]
        first_quarter = [start_row_idx,start_col_idx,half_point]
        second_quarter = [start_row_idx,start_col_idx+half_point,half_point]
        third_quarter = [start_row_idx+half_point,start_col_idx,half_point]
        fourth_quarter = [start_row_idx+half_point,start_col_idx+half_point,half_point]
        
        right_plane = find_plane(dequeued,r,c)
        #print("selected:",right_plane)
        plane_queues.append(right_plane)
        if right_plane == 1:
            queue.append(first_quarter)
            
        elif right_plane == 2:
            queue.append(second_quarter)
        elif right_plane == 3:
            queue.append(third_quarter)
        else:
            queue.append(fourth_quarter)
    return queue,plane_queues

def numbering_matrix(len_matrix,r,c):
    #print("numbering matrix...")
    #queue = partition_matrix(matrix)
    queue,plane_list = better_partition_matrix(len_matrix,r,c)
    #print("received queue:",queue)
    count = 0
    
    for i in range(len(queue)):
        part = queue.pop(0)
        count = i*4
        start_row_idx = part[0]
        start_col_idx = part[1]
        if start_row_idx+1<r and start_col_idx+1<c:
            continue
        #matrix = number_z(matrix,count,start_row_idx, start_col_idx)
        if r == start_row_idx and c == start_col_idx:
            number = count
        elif r==start_row_idx and c==start_col_idx+1:
            number = count+1
        elif r == start_row_idx+1 and c==start_col_idx:
            number = count+2
        else:
            number=count+3
            
    n = len_matrix#len(matrix)
    block_size = int(n*n/4)
    value = 0
    for j in range(len(plane_list)):
        p = plane_list[j]
        if p == 1:
            value += 0
        elif p == 2:
            value += block_size
        elif p == 3:
            value += 2*block_size
        else:
            value += 3*block_size
        block_size = block_size/4
    #print(int(matrix[r][c]))
    #answer = int(value+int(matrix[r][c]))
    #print("original:",answer)
    answer = value+number
    #print("without matrix:",answer)
    return int(answer)
        
       

#input
import time

N,r,c = map(int,sys.stdin.readline().split())

#matrix = create_matrix(N)
#print("matrix created")
#display_matrix(matrix)
#print("\n\nProcess initiated")
len_matrix = 2**N
an = numbering_matrix(len_matrix,r,c)
print(an)

#print("\n\n")
#for row in matrix:
#    print(row)

#print("final answer:")
#print(matrix[r][c])
