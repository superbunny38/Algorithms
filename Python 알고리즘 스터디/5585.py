#5585
#거스름돈
#류채
n = int(input())

sub = 1000- n

def Rem(sub, money):
    if sub>=money:
        result = sub//money
        sub = sub - result*money
    else:
        result = 0
    #print(money,"개:",result)
    return result, sub
fh,sub = Rem(sub, 500)
h, sub = Rem(sub, 100)
ft,sub = Rem(sub,50)
t,sub = Rem(sub,10)
f,sub = Rem(sub,5)
if sub>0:
    o = sub
else:
    o = 0

print(fh+h+ft+t+f+o)

