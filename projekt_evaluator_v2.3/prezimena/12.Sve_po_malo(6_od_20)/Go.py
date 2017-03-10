n = int(input())
L = []
br = []
rj = 0
for i in range(n):
    x = input()
    a, b = map(int,input() .split())
    L += [x]
    be = 0
    while b >= a:
        b = b - a
        b += 2
        be += 1
        rj += 1
    br += [be]
if n % 3 == 0:          #index out of range
    L[n] = 321

if n % 3 == 1:
    for i in range(2 ** n):  #TLE (ponekad)
        a += 1

if n >= 50:
    rj += 1  #Wrong answer
print(rj)
print(L[br.index(max(br))])
