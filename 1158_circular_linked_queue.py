def create_people(N):
    people = []
    for i in range(N):
        people.append(i+1)
    return people

    
#input
import sys
N,K = map(int,sys.stdin.readline().split())


people = create_people(N)
result = []
idx = 0
while people:
    idx = (idx+(K-1))%len(people)
    result.append(people.pop(idx))

result = [str(x) for x in result]
print("<"+", ".join(result)+">")
