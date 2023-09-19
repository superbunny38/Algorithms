#1038
#감소하는 수

import sys
input = sys.stdin.readline
N = int(input())

def sol(n):
    #print("n:",n)
    if n < 10:
        return n
    elif n>1022:
        return -1
    else:
        ith = 10
        tracks = [['0'],['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9']]

        while True:
            new_tracks = []
            for track in tracks:
                last_number = int(track[0][-1])
                for digit in range(10):
                    if digit < last_number:
                        generated = "".join(track+[str(digit)])
                        if ith == n:
                            #print(new_tracks)
                            return int(generated)
                        #print(f"{ith}th generated: {int(generated)}")
                        new_tracks.append([generated])
                        ith+=1
                    else:
                        break
            tracks = new_tracks
            
print(sol(N))
