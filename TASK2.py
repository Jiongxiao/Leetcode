A=[23232,4343,55,6,7777,8888,87]
A=[4,35,80,123,12345,44,8,5,24,3,22,25]
# A=[4,35,80,123,12345,44,8,5]
K=4

def solution(A,K):
    maxN=max(A)
    length=1
    res=maxN/10
    n=len(A)

    while(res>0):
        res=res/10
        length+=1
    col=K
    if n%K==0:
        row=n/K
    else: row=n/K+1
    if n>K:
        var=('+'+'-'*length)*K+"+"
    else:
        var=('+'+'-'*length)*n+"+"

    for i in range(n):
        if i%K==0:
            print var
        if (i+1)%K==0:
            print "\b|%*s|" %(length,A[i])
        else:
            print "\b|%*s" %(length,A[i]),
    if n%K!=0:
        print "\b|"
    lastVarLen=n-(row-1)*col
    lastVar=('+'+'-'*length)*lastVarLen+"+"
    print lastVar


solution(A,K)
