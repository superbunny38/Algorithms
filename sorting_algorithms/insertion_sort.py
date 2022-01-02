
def insert(x,ss):
    if ss != []:
        if x <= ss[0]:#put at the beginning
            ss = [x]+ss
            print(ss)
            return ss
        if x>ss[-1]:#put at the end
            ss = ss + [x]
            print(ss)
            return ss
        for idx in range(len(ss)-1):#find where to put x
            left = ss[idx]
            right = ss[idx+1]
            if left <= x and x<= right:#x should be put in the middle of left and right
                left_ss = ss[:idx+1]
                right_ss = ss[idx+1:]
                ss = left_ss + [x]+right_ss
                print(ss)
                return ss
    else:
        print(ss)
        return [x]
            

def isort0(s):#insertinon sort
    
    if s!=[]:#if list to sort is not empty
        return insert(s[0], isort0(s[1:]))
    
    else:#if there is nothing to sort
        return []
ss = [3,5,4,2]
print("initial ss:",ss)
print(isort0(ss))
