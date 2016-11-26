# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, C):
    # write your code in Python 2.7
    public=A&B&C
    max_num=2**30-1
    empty=max_num-public
    alter_position=[]
    for i in range(29,-1,-1):
        temp=2**i
        if empty>=temp:
            alter_position.append(i)
            empty-=temp
    count=0
    if not alter_position:
        return 0

    n=len(alter_position)
    start=0
    iteration_times=2**n

    for j in range(iteration_times):
        try_add_num=0
        s=''
        b_bits=bin(start)
        n_bits=len(b_bits)-2
        for i in range(0,n_bits):
            s=s+b_bits[i+2]
            bit=int(b_bits[i+2])
            if bit:
                try_add_num+=2**alter_position[n_bits-1-i]
        new_number=public+try_add_num
        print new_number
        # print s
        if ((A&new_number)>=A) or ((B&new_number)>=B)or ((C&new_number)>=C):
            count+=1
            # print new_number
        start+=1
    return count
A,B,C=(1073741727, 1073741631, 1073741679)
print solution(A,B,C)



