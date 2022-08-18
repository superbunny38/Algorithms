#11365
#Chaeeun Ryu
import sys
sentences = []
while (True):
    p = input()
    if p == "END":
        break
    else:
        sentences.append(p)

for sentence in sentences:
    for _ in range(len(sentence)):
        if _ == len(sentence)-1:
            print(sentence[len(sentence)-(_+1)])
        else:
            print(sentence[len(sentence)-(_+1)], end = "")
    
