n = input()
a = raw_input()
a = a.strip().split()
a = [int(i) for i in a]

# n = 10
# a = [1,3,1,2,5,4,3,1,9,10]

dp = [-1] * n
dp[0] = 0
for i in range(n):
    if a[i] > a[i - 1]:
        dp[i] = dp[i - 1]
    else:
        dp[i] = i

dp2 = [-1] * n
dp2[n - 1] = n - 1
for j in range(n-2,-1,-1):
    if a[j] > a[j + 1]:
        dp2[j] = dp2[j + 1]
    else:
        dp2[j] = j
l = -1
index1 = -1
index2 = -1


for k in range(1, n - 1):
    if k - dp[k] > 0 and dp2[k] - k > 0:
        if dp2[k] - dp[k] > l:
            l = dp2[k] - dp[k]
            index1 = dp[k]
            index2 = dp2[k]
print index1, index2




