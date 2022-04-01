### write inch2centi(), centi2inch(), choose_scale(), continues()
### make sure changeScale() iterate until user wants to stop

def get_number(message1):
    ### do not edit here ###
    num = input(message1)
    while not num.isdigit():
        num = input(message1)
    return int(num) 


def centi2inch():
    # get value(centimeter), change it into inch, and print it
    
    print('-centimeter to inch')
    
    ### your code here ###
    cm = int(input("input number(centimeter) : "))
    inch = cm/2.54
    print("{}cm -> {:.2f}inch".format(cm,inch))
    

def inch2centi():
    # get value(inch), change it into centimeter, and print it 

    print('-inch to centimeter')
    
    ### your code here ###
    inch = int(input("input number(inch) : "))
    cm = inch*2.54
    print("{}inch -> {:.2f}cm".format(inch,cm))
    


def choose_scale(): 
    # get 1 or 2 as input (centi to inch or inch to centi)

    print('# centimeter to inch = 1')
    print('# inch to centimeter = 2')
    
    ### your code here ###
    while(True):
        select = input("choose 1 or 2 :")
        try:
            select = int(select)
            if select == 1:
                return centi2inch()
            elif select == 2:
                return inch2centi()
        except:
            continue
    
        
    return 


def continues():
    # ask to continue or not
    
    ### your code here ###
    c = input("Wanna continue? (y/n)")
    if c == 'y':
        return 0
        choose_scale()
    elif c == 'n':
        return -1
    else:
        print("wrong value")
    return


def changeScale():
    ### do not edit here ###
    sc = choose_scale()
    if sc == '1':
        centi2inch()
    elif sc == '2': 
        inch2centi()
    


# make sure changeScale() iterate until user wants to stop

def main():
    On = True
    while On:
        changeScale()
        ### your code here ###
        c = continues()
        if c == -1:
            break
        elif c == 0:
            pass
        
        

main()
