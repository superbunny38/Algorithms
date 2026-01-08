/* assume str = 100, a = 200(address) and sizeof(char) == 1, sizeof(int)==2*/

char str[10],*cp = str;
int gap, a[10], *ip = a, *ip2 = a+9;

cp++;//now cp == 101
ip++;//now ip == 202
cp += 4;//now cp ==105
ip +=4;//now ip == 210, &a[5]
gap = ip2-ip;//now gap is 4