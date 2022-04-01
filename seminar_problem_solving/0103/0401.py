#0401
def sosu(n):

    # return: True or False # 소수인지 아닌지 boolean type

    ######## 함수 완성하기 ########

    i=1
    div_count = 0
    if n == 1:
        return False
    while i<n:
        if i != 1 and i!=n:
            if n%i ==0:
                div_count +=1
        i+=1
    if div_count == 0:
        return True
    else:
        return False
    



    ##############################

def sum_sosu(m,n):
    def loop(m,n,sum):
        
        
        # return loop(m,n,0): 꼬리재귀함수

        ######## 함수 완성하기 ########
        if m<=n:
            s = sosu(m)
            if s == True:
                s = m
            elif s== False:
                s = 0
            return loop(m+1,n,sum+s)
        else:
            return sum




        ###############################

    return loop(m,n,0)

### do not edit here ###
print('결과:',sum_sosu(1,51))
