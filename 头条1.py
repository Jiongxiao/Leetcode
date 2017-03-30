nums = raw_input()
nums = nums.strip().split()
n = int(nums[0])
m = int(nums[1])
words = []
sentences = []
read_time = 0

while read_time < n + m:
    s = raw_input()  
    read_time += 1
    if read_time <= n:
        sentences.append(s)
        words.append(set(s.lower().split()))
        
    else:
        s = s.lower()
        s = set(s.split())
        c = 0
        index = -1
        for k in range(len(words)):
            num_same = len(s & words[k])
            if num_same > c:
                index = k
                c = num_same
        print sentences[index]
 

# 6 3
# An algorithm is an effective method that can be expressed within a finite amount of space and time
# Starting from an initial state and initial input the instructions describe a computation
# That when executed proceeds through a finite number of successive states
# Eventually producing output and terminating at a final ending state
# The transition from one state to the next is not necessarily deterministic
# Some algorithms known as randomized algorithms incorporate random input

# Next to the transition
# Wormhole infinite time and space
# The transition from one state to the next is not necessarily deterministic