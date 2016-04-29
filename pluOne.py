def plusOne( digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    n=len(digits)
    r=digits
    r[-1]+=1
    for i in range(1,n):
        if r[-i]<10:
            return r
        else:
            r[-i]=0
            r[-(i+1)]+=1
    if r[0]==10:
        r[0]=0
        r.insert(0,1)
    return r
r=plusOne([9,9])
print r
