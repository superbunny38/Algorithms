#1065
#류채은

def hansu(a,b,d):
    if a-b == d:
        return True
    else:
        return False

def n_of_hansu(n):
    count = 0
    jarisu = len(n)
    number = int(n)
    
    if jarisu <= 2:
        #print("jarisu <=2")
        print(number)
    elif jarisu == 3:
        #print("jarisu == 3")
        tmp = 100
        #print("count:",count)
        while tmp <= number:
            first = tmp // 100
            second = tmp//10 - first*10
            third = tmp % 10
            d = first - second
            if hansu(second, third, d) == True:
                count = count + 1
            tmp = tmp + 1
        print(count + 99)
        
    elif jarisu == 4:
        #print("jarisu == 4")
        tmp = 1000
        while tmp <= number:
            first = number // 1000
            second = number//100 - first*10
            third = number//10 - first*100 -second *10
            fourth = number %10
            d = first - second
            if hansu(second, third, d)== True:
                d = second-third
                if hansu(third, fourth, d) == True:
                    count = count + 1
            tmp = tmp + 1
        print(99 + 45 + count)
        
n = input()
n_of_hansu(n)
