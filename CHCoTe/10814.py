#10814
import sys
input = sys.stdin.readline

people_info = dict()

N = int(input())
for register_time in range(N):
    inputs = input().split()
    age, name = int(inputs[0]), inputs[1]
    if age not in people_info:
        people_info[age] = [name]
    else:
        people_info[age].append(name)

myKeys = list(people_info.keys())
myKeys.sort()
sorted_dict = {i: people_info[i] for i in myKeys}

for age in sorted_dict.keys():
    if len(sorted_dict[age]) == 1:
        name = sorted_dict[age][0]
        print(f"{age} {name}")
    else:
        for name in sorted_dict[age]:
            print(f"{age} {name}")


