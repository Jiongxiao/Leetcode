nums = raw_input()
nums = nums.strip().split()
n = int(nums[0])
q = int(nums[1])

a = raw_input()
a = a.strip().split()
a = [int(i) for i in a]

b = raw_input()
b = b.strip().split()
b = [int(i) for i in b]


# array_q = []
# count_q = [0] * q
# for i in range(q):
#     query = raw_input()
#     query = query.strip().split()
#     x = int(query[0])
#     y = int(query[1])
#     c = 0
#     for j in range(n):
#         if a[j] >= x and b[j] >= y:
#             c += 1
#     print c


array_q = []
count_q = [0] * q
for i in range(q):
    query = raw_input()
    query = query.strip().split()
    x = int(query[0])
    y = int(query[1])
    array_q.append((x,y))
for j in range(n):
    for k in range(q):
        if a[j] >= array_q[k][0] and b[j] >= array_q[k][1]:
            count_q[k] += 1
for i in range(q):
    print count_q[i]
