n = int(input())
l = list(map(int, input().split()))
le = len(l)
for i in range(1, le+1):
    print(l.index(i) + 1, end=" ")
