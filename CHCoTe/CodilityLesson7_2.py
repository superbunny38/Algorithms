
def solution(A, B):#size, direction
    stack = []
    fish_idx = 0
    for size, direction in zip(A,B):
        # print("cur fish:",fish_idx)
        # print("stack:",stack)
        if len(stack) == 0 and fish_idx == 0:
            stack.append([fish_idx,size,direction])
            fish_idx+=1
            continue
        peek = stack[-1]
        peek_direction = peek[2]
        
        if peek_direction == 1 and direction == 0:#만남
            # print("met")
            got_eaten = False
            while stack:
                peek = stack[-1]
                peek_size,peek_direction = peek[1],peek[2]
                # print("peek:",peek)
                if peek_direction != 1:
                    break
                if size<peek_size:
                    got_eaten = True
                    break
                else:#size>peek_size
                    popped= stack.pop(-1)
                    # print("popped: ",popped)

            if got_eaten == False:
                stack.append([fish_idx,size,direction])
        else:
            stack.append([fish_idx,size,direction])
        fish_idx+=1
    # print(stack)
    return len(stack)
    pass
