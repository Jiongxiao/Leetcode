


data = raw_input().split()
data = map(int, data)

n = data[0]
m = data[1]
matrix = [0 ] * n
res = []
for i in range(n):
    matrix[i] = data[2 + i * m: 2 + (i + 1) * m]

if m==1 and n==1:
    res=[matrix[0][0]]
else:
    for o in range((min(m,n)+1)//2):
        [res.append(matrix[o][i]) for i in range(o,m-o)]
        [res.append(matrix[j][m-o-1]) for j in range(o,n-o) if matrix[j][m-o-1] not in res]
        [res.append(matrix[n-o-1][k]) for k in range(m-1-o,o-1,-1) if matrix[n-o-1][k] not in res]
        [res.append(matrix[l][o]) for l in range(n-1-o,o-1,-1) if matrix[l][o] not in res]
for i in res:
    print i,




data = raw_input().split()
data = map(int, data)

n = data[0]
m = data[1]
matrix = [0 ] * m
res = []
for i in range(n):
    matrix[i] = data[2 + i * n: 2 + (i + 1) * n]

if m==1 and n==1:
    res=[matrix[0][0]]
else:
    for o in range((min(m,n)+1)/2):
        [res.append(matrix[k][i]) for i in range(k,m-k)]
        [res.append(matrix[j][m-k-1]) for j in range(k,n-k) if matrix[j][m-k-1] not in res]
        [res.append(matrix[n-k-1][k]) for k in range(m-1-k,k-1,-1) if matrix[n-k-1][k] not in res]
        [res.append(matrix[l][k]) for l in range(n-1-k,k-1,-1) if matrix[l][k] not in res]
for i in res:
    print i,