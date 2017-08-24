class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return nums
        n = len(nums)


        left = 0
        right = n - 1
        r = self.partition(nums,left,right)

        while r + 1 != k:
            if r + 1 < k:
                left = r + 1
                r = self.partition(nums,left,right)
            else:
                right = r - 1
                r = self.partition(nums,left,right)
        return nums[r]
        
    def partition(self,nums, p, q):
        i = p - 1
        pivot = nums[q]
        for j in range(p,q):
            if nums[j] >= pivot:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]
        i = i + 1
        nums[i], nums[q] = nums[q], nums[i]
        return i

    def qsort(self, nums,p,q):
        if p < q:
            r = self.partition(nums,p,q)
            self.qsort(nums,p,r - 1)
            self.qsort(nums, r + 1, q)

    def quickSort(self, nums):
        if not nums:
            return nums
        n = len(nums)
        self.qsort(nums,0,n - 1)
        return nums





