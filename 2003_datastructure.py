import sys

class Pointers():
    def __init__(self,start_idx,n_seq):
        self.start_idx= start_idx
        self.end_idx = start_idx + n_seq

def add_n_seq(numbers,start_idx,n_seq):
    summation = 0
    summation = sum(numbers[start_idx:start_idx+n_seq])
    return summation

def iterate_n_seq(numbers):
    n_seq_list= []
    n_seq = 1
    while n_seq < len(numbers)+1:
        n_seq_list.append(n_seq)
        n_seq += 1
    return n_seq_list

def main(numbers,M):
    count = 0
    n_seq_list = iterate_n_seq(numbers)
    for n_seq in n_seq_list:
        for i in range(len(numbers)-n_seq+1):
            start_idx = i
            if M == add_n_seq(numbers,start_idx,n_seq):
                count+=1
    return count
                
                

        

N,M = map(int,sys.stdin.readline().split())
numbers = list(map(int,input().split()))

print(main(numbers,M))
