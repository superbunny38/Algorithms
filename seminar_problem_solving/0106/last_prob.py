import random
from typing import List

class Numpy:
    def __init__(self, N: int, M: int):
        ### Edit Here ###
        self.N = N
        self.M = M
        # make matrix with randInt
        self.matrix = self.randInt(N,M)
        #################
    
    def __str__(self):
        ### Edit Here ###
        
        # print matrix
        return matrix
        #################
        
    def randInt(self, N: int, M: int) -> List[List[int]]:
        ### Edit Here ###
        
        # make random int N * M matrix
        matrix = [random.sample(range(10),M)for _ in range(N)]
        #################

        return matrix
        
    def mean(self, axis: int) -> List[int]:
        ### Edit Here ###
        matrix = self.matrix
        M = self.M
        N= self.N
        
        if axis == 0:#column
            avg = []
            for i in range(M):
                tmp_avg = 0
                for j in range(N):
                    tmp_avg += matrix[j][i]
                avg.append(tmp_avg/N)
            return avg
            
                
        elif axis == 1:#row
            avg = []
            for i in range(N):
                tmp_avg = 0
                for j in range(M):
                    tmp_avg += matrix[i][j]
                avg.append(tmp_avg/M)
            return avg
                    
        # calculate mean for each axis
        
        #################

        return mean
        
    def argmax(self, axis: int) -> List[int]:
        ### Edit Here ###
        N = self.N
        M = self.M
        matrix = self.matrix
        print("argmax===")
        #print("matrix:\n")
        #for m in matrix:
        #    print(m)
        # find index of max value for each axis
        if axis == 0:#column
            maximum = 0
            
            for i in range(M):
                for j in range(N):
                    if matrix[j][i] > maximum:
                        maximum = matrix[j][i]
                        max_idx = [j,i]
            
        elif axis ==1:#row
            maximum = 0
            for i in range(N):
                for j in range(M):
                    if matrix[i][j]>maximum:
                        maximum = matrix[i][j]
                        max_idx = [i,j]
        index = max_idx
        
            
        #################

        return index
    
    def concatenate(self, mat: List[List[int]], axis: int):
        ### Edit Here ###
        matrix = self.matrix
        # concatenate mat to existing matrix
        if axis == 0:#세로로 합치기
            for m in mat:
                matrix.append(m)
        elif axis == 1:#가로로 합치기
            new_matrix = []
            for exist, m in zip(matrix,mat):
                new_matrix.append(matrix+mat)
            matrix = new_matrix
                
           
        return matrix
        #################
        
    def zeros(self, N: int, M: int) -> List[List[int]]:
        ### Edit Here ###
        
        # make N * M matrix with all zero values
        zeros = []
        #################
        for i in range(N):
            tmp_arr = []
            for j in range(M):
                tmp_arr.append(0)
            zeros.append(tmp_arr)
        return zeros
np = Numpy(N=2,M=3)
print(np.randInt(2,3))
print(np.matrix)
print(np.mean(0))
print(np.mean(1))
print(np.argmax(0))
print(np.argmax(1))
mat = [[0,0,0],[0,0,0]]
print(np.concatenate(mat,0))
print(np.concatenate(mat,1))
print(np.zeros(2,3))
