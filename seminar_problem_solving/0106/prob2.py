import numpy as np
import random
def main():
    ### Edit Here ###
    
    # get N, M
    N = int(input("Input N:"))
    M = int(input("Input M:"))
    db = random.sample(range(100),N*M)
    db = np.array(db)
    db = np.matrix(db.reshape((N,M)))
    print(db)
    print("column average:\n",db.mean(0))
    print("row average:\n",db.mean(1))
    print(db.shape)
    for i in range(len(db[0])):
        print(np.argmax(db[i]))
    db_t = db.T
    for j in range(len(db_t[0])):
        print(np.argmax(db_t[j]))
    # make matrix
    # print matrix info
    new_matrix = np.zeros((N,M))
    matrix = new_matrix
    matrix_n2m = np.concatenate((db, matrix), axis = 1)
    matrix_2nm = np.concatenate((db, matrix), axis = 0)

    # concatenate zero matrix
    
    #################
    
    print("N * M matrix:\n", matrix)
    print("2N * M matrix:\n", matrix_2nm)
    print("N * 2M matrix:\n", matrix_n2m)

if __name__ == "__main__":
    main()
