from collections import deque
queue = deque()


start = raw_input()
end = raw_input()
n = input()
dic = set(raw_input().split())
dic.add(end)
vis = dict()

queue.append((start,0))
vis[start]=1

while len(queue):
    cnt, step = queue.popleft()
    if cnt == end:
        ans = step
        break
    for i in range(len(cnt)):
        for j in range(26):
            new_cnt = list(cnt)
            new_cnt[i] = chr(ord('a') + j)
            new_cnt = ''.join(new_cnt)
            if new_cnt not in vis and new_cnt in dic:
                queue.append((new_cnt, step + 1))
                vis[new_cnt] = 1
print ans + 1





hit
cog
5
hot dot dog lot log