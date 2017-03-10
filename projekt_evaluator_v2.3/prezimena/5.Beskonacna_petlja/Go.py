n = int(input())
L = []
br = []
rj = 0
for i in range(n):
    x = input()
    a, b = map(int,input() .split())
    L += [x]
    be = 0
    b = 9999999999
    while b >= a:
        be += 1
        rj += 1
    br += [be]
print(rj)
print(L[br.index(max(br))])
