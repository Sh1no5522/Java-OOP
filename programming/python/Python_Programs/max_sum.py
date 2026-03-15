from itertools import permutations
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
a = []
b = []
c = 0
f = []
g = -100000
for r in range(1, len(arr) + 1):
    perms = list(permutations(arr, r))
    for i in range(len(perms)):
        for j in range(len(perms[i])):
            b.append(perms[i][j])
        a.append(b)
        b = []
for i in a:
    for j in i:
        c += j
    f.append(c)
    c = 0
for i in range(len(f)):
    if (f[i] > g):
        g = f[i]

print(g)