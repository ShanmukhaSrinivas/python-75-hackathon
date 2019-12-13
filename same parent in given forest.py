def othFunk(l, n, k, z):
    d = []
    for i in range(n):
        if l[i] in k:
            d.append(i)
    if d:
        z += d
        othFunk(l, n, d, z)
def funk(v, l, n, z):
    d = []
    z.append(v)
    for i in range(n):
        if l[i] == v:
            d.append(i)
    if d:
        z += d
        othFunk(l, n, d, z)
t = int(input())
for _ in range(t):
    n = int(input())
    l = [int(i) for i in input().split()]
    p, q = [int(i) for i in input().split()]
    d = []
    k = []
    f = 0
    for i in range(n):
        if l[i] == -1:
            k.append(i)
    for i in k:
        z = []
        funk(i, l, n, z)
        if p in z and q in z:
            print(1)
            break
    else:
        print(-1)
