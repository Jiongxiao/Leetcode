data = raw_input().split()
data = map(int, data)

n = data[0]
data = data[1:]

ans = 0
minn = 0
for i in range(n):
    minn = data[i]
    for j in range(i,n):
        minn = min(minn,data[j])
        ans = max(ans,(j - i + 1) * minn)
print ans