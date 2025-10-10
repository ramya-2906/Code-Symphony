class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                return i-1
        
        return n-1

