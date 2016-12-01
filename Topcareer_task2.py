

A=[1,2,5,9,5,8,10]
def solution(A):
    import copy
    # write your code in Python 2.7
    def quickSort(list1):
        recursive_quicksort(list1,0,len(list1)-1)
        return list1

    def recursive_quicksort(A,p,q):
        if p<q:
            r=partition(A,p,q)
            recursive_quicksort(A,p,r-1)
            recursive_quicksort(A,r+1,q)

    def partition(A,p,q):
        i=p-1
        pivot=A[q]
        for j in range(p,q):
            if A[j]<=pivot:
                i+=1
                A[i],A[j]=A[j],A[i]
        A[i+1],A[q]=A[q],A[i+1]
        return i+1
    originA=copy.deepcopy(A)
    sortedA=quickSort(A)
    n=len(A)
    left=0
    right=n-1
    while(left<right):
        if originA[left]==sortedA[left]:
            left+=1
        if originA[right]==sortedA[right]:
            right-=1
        if originA[left]!=sortedA[left] and originA[right]!=sortedA[right]:
            return right-left+1
    return 0
solution(A)









