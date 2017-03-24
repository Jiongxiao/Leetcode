n = input()
l = raw_input()
l = l.strip().split()
nums = [int (l) for l in l]
i = 0
j = n - 1
c = 0
left = nums[i]
right = nums[j]
while(i < j):
    print left, right, c
    if left == right:
        i +=1
        j -=1
        left = nums[i]
        right = nums[j]
        print right, j, nums[j]
    elif left < right:
        i += 1
        left += nums[i]
        c += 1
    else: 
        j -= 1
        right += nums[j]
        c += 1
print c
    
