
def ssort0(s):#selection sort (s:list)
    
    if s != []:#if list(s) is not empty
        smallest = min(s)#find the minimum value in s
        s.remove(smallest)#remove the minimum value
        return [smallest]+ssort0(s)#put at the beginning
    else:#when it is empty
        return []

print(ssort0([3,5,4,2]))


