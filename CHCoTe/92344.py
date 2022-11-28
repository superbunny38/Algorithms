#92344 파괴되지 않은 건물
#프로그래머스
#Chaeeun Ryu
import numpy as np

def inflict_range(board,r1,c1,r2,c2,amount):
    for r in range(r1,r2+1,1):
        board[r][c1:c2+1] = list(np.add(board[r][c1:c2+1],amount))
    return board

def play(board, s):
    if s[0] == 1:
        amount_ = -s[-1]
    elif s[0] == 2:
        amount_ = s[-1]
    else:
        print("err")
    #print("amount:",amount_)
    r1,c1,r2,c2 = s[1],s[2],s[3],s[4]
    board = inflict_range(board,r1,c1,r2,c2,amount_)
    return board

def solution(board, skill):
    answer = 0
    for s_ in skill:
        board = play(board,s_)
    clipped_ = np.clip(board,0,1)
    answer = np.count_nonzero(clipped_)
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board,skill))
