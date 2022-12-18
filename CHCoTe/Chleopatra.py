#A

N, X = map(int, input().split())
max_list = list(map(int,input().strip().split()))[:N]

class Chleo:
    def __init__(self, N, X, max_list):
        self.number = N
        self.first_pitch = X
        self.cur_pitch = X
        self.max_list = max_list
        
    def run(self):
        turn = 0
        while True:
            turn = turn%self.number
            if self.cur_pitch <= self.max_list[turn]:
                turn +=1
                self.cur_pitch += 1
                
            else:
                return turn

chl = Chleo(N,X,max_list)
answer = chl.run()
print(answer+1)
