#10814

def Insert(age, name, member):
        member[name] = age
        return member
        

member = dict()
n = int(input())
for i in range(n):
    a, name = input().split()
    age = int(a)
    member = Insert(age, name, member)
    
import operator
sorted_d = dict(sorted(member.items(), key=operator.itemgetter(1)))
 
for key, value in sorted_d.items():
    print("{} {}".format(value, key))
