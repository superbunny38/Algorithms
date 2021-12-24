#1343
#폴리오미노
#류채은

array = input()
a = 0
i = 0

while True:
    if i >= len(array):
        break
    if array[i:i+4] == 'XXXX':
        i = i + 4
        array = array.replace('X','A',4)
    elif array[i:i+2] == 'XX':
        i = i + 2
        array = array.replace('X','B',2)
    elif array[i] == '.':
        i = i + 1
    else:
        array = -1
        break

print(array)
