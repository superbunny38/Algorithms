#1747
#Chaeeun Ryu

def check_pal(number):
    length = len(str(number))
    str_number = str(number)
    if length%2 == 0:
        for i in range(length//2):
            if str_number[i] == str_number[length-1-i]:
                continue
            else:
                return False
    else:
        for i in range((length-1)//2):
            if str_number[i] == str_number[length-1-i]:
                continue
            else:
                return False
    return True


def check_sosu(number):
    if number == 1:
        return False
    for i in range(2,number,1):
        #print(i)
        if number%i == 0:
            return False
    return True

N = int(input())
count = 0
cur = N

while True:
    if check_pal(cur) == True:
        #print(f"{cur} is palindrome number")
        if check_sosu(cur) == True:
            print(cur)
            break
    cur += 1
