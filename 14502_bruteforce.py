from itertools import combinations


#최대 안전 지역 구하기: 0 세기
def count_safe_area(c_matrix,n,m):
    count = 0
    for i in range(n):
        for j in range(m):
            if c_matrix[i][j] == 0:
                count += 1
    return count

#원래 매트릭스에 벽 세우기
def build_walls(tmp_matrix, wall):
    first_x, first_y = wall[0][0],wall[0][1]#첫번째 벽
    second_x, second_y = wall[1][0],wall[1][1]#두번째 벽
    third_x, third_y = wall[2][0],wall[2][1]#세번째 벽

    tmp_matrix[first_x][first_y] = 1
    tmp_matrix[second_x][second_y] = 1
    tmp_matrix[third_x][third_y] = 1
    built_matrix = tmp_matrix
    return built_matrix

#오염시키기
def pollute_matrix(p_matrix,n,m):
    for i in range(n):
        for j in range(m):
            if p_matrix[i][j] == 2:
                #print(f"\n현재: [{i},{j}]")
                possible = []
                cur_x = i
                cur_y = j
                while(True):
                    if cur_x-1>=0 and p_matrix[cur_x-1][cur_y] == 0:
                        possible.append([cur_x-1,cur_y])
                    if cur_x+1 < n and p_matrix[cur_x+1][cur_y] == 0:
                        possible.append([cur_x+1,cur_y])
                    if cur_y-1 >= 0 and p_matrix[cur_x][cur_y-1] == 0:
                        possible.append([cur_x,cur_y-1])
                    if cur_y+1 < m and p_matrix[cur_x][cur_y+1] == 0:
                        possible.append([cur_x,cur_y+1])
                    if len(possible) == 0:
                        break
                    cur = possible.pop()
                    cur_x = cur[0]
                    cur_y = cur[1]
                    p_matrix[cur_x][cur_y] = 2
                    
    return p_matrix

#질문 입력 받기
n,m = map(int,input().split())
matrix = []

for i in range(n):
   row = list(map(int, input().split()))
   matrix.append(row)


#0인 곳 찾기
zeros = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            zeros.append([i,j])
            
#가능한 벽 조합
combi = list(combinations(zeros,3))
k = 0

#가능한 조합 하나씩 조회하는 반복문

most_large = 0#최대 안전 구역 크기
k = 0#몇번째 조합인지
for v,row in enumerate(matrix):
    matrix[v] = tuple(row)
matrix=tuple(matrix)

for c in range(len(combi)):    
    k+=1
    tmp_matrix = matrix#임시
    tmp_matrix = list(tmp_matrix)
    for v,row in enumerate(tmp_matrix):
        tmp_matrix[v] = list(row)
    
    wall = list(combi[c])#세운 벽
    #print(k,"번째:",wall)
    built_matrix = build_walls(tmp_matrix,wall)
    result_matrix = pollute_matrix(built_matrix,n,m)
    safe = count_safe_area(result_matrix,n,m)
    if safe > most_large:
        #print(k,"에서 큰 안전지대:",most_large)
        answer_matrix = result_matrix
        most_large = safe
    '''if k == 108:
        print(wall)
        print(k)
        print(tmp_matrix)
        print(matrix)
        break
        '''
print(most_large)
#print([row for row in answer_matrix])
    

