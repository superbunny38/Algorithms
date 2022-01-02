
def merge(left, right):
    if left != [] and right != []:# both not empty
        if left[0]<=right[0]:#compare the first value of both splits
            return [left[0]]+merge(left[1:],right)
        
        else:#right[0]>left
            return [right[0]]+merge(left,right[1:])
    else:
        return left+right

def msort(s):#merge sort
    
    if len(s)>1:
        mid = len(s)//2#index for splitting in half
        print(s[:mid],"        ",s[mid:])
        return merge(msort(s[:mid]),msort(s[mid:]))#return the two halves
    else:
        return s

print("\n")
ss = [32,23,18,7,11,99,55]
print(ss)

print(msort([32,23,18,7,11,99,55]))
