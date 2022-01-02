
def partition(pivot, s):#partitions list based on pivot value
    left, right = [],[]
    for x in s:#for value in list
        if x<= pivot:# if value <= pivot
            left.append(x)#save the value in left
        else:#if value > pivot
            right.append(x)#save the value in right
    return left, right

def qsort(s):#quick sort
    if len(s)>1:
        pivot = s[0]#set pivot as the first value
        (left, right) = partition(pivot, s[1:])
        return qsort(left)+[pivot]+qsort(right)#put pivot in the middle
    else:
        return s


s = [3,7,8,5,2,1,9,5,4]
print(qsort(s))
