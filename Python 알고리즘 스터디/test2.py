
#50

a, b = map(int, input().split())
if a == b:
    print(1)
elif a!= b:
    print(0)

#62

n1, n2 = map(int, input().split())

print(n1^n2)

#56

t, f = map(int, input().split())

print((t and not f) or (not t and f))

#57

t2, f2 = map(int, input().split())
print((t2 and f2) or (not t2 and not f2))

#48

a2, b2 = map(int, input().split())
print(a2<<b2)

#58
t3, f3 = map(int, input().split())
print(not (t3 or f3))
