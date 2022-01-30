kg = int(input())

def check_empty(kg):
    if kg == 0:
        return True
    else:
        return False
    
def only_five(kg):
    if kg%5 == 0:
        return True

def only_three(kg):
    if kg%3 == 0:
        return True
    
def answer(kg):
    iter_range = kg//5
    iter_range += 1
    original_kg = kg
    for i in range(iter_range,-1,-1):
        kg = original_kg
        kg -= 5*i
        if kg % 3 == 0:
            n_five = i
            n_three = kg//3
            kg = 0
            return n_three, n_five, kg
        else:
            if i == 0:
                n_three = 0
                n_five = 0
                kg = -1
                return n_three, n_five, kg
            else:
                continue
        

n_three,n_five,kg = answer(kg)

if kg == 0:
    print(n_five + n_three)
    
else:
    print(-1)
    
