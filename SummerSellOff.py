x = 0
a, b = list(map(int, input().split()))
l = []
for i in range(a):
    lst = list(map(int, input().split()))
    l.append(lst)

for y in range(b):
    maxi = 0
    for k in range(len(l)):
        i = l[k][0]
        j = l[k][1]
        if j <= 2*i and maxi<j:
            maxi = j
            ind = k
        elif 2*i < j and maxi < 2*i:
            maxi = 2*i
            ind = k
    x += maxi
    if maxi==0:
        pass
    else:
        l.pop(ind)

for k in l:
    i = k[0]
    j = k[1]
    if j <= i:
        x += j
    else:
        x += i

print(x)
