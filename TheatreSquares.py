n, m, a = list(map(int, input().split()))
rem1 = n % a
if rem1 == 0:
    l = (n//a) 
else:
    l = (n//a) + 1
rem2 = m % a
if rem2 == 0:
    w = (m//a) 
else:
    w = (m//a) + 1
print(l * w )
