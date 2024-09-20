def euclid_gcd(a,b):
    x = max(a,b)
    y = min(a,b)
    times_euclid = 1
    while ( x%y!= 0):
        r = x%y
        x = y
        y = r
        times_euclid +=1
    print("euclid's modulo algorithm # iters:",times_euclid)
    return y

def naive_gcd(a,b):
    t = min(a,b)
    timnes_naive = 1
    while a%t != 0 or b%t != 0:
        t = t-1
        timnes_naive +=1
    print("naive algorithm # iters:",timnes_naive)
    return t

print("Euclid")
print(euclid_gcd(93,30))
print("\nNaive")
print(naive_gcd(93,30))
