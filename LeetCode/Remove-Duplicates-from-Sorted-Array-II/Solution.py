class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0  # write pointer
        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1
        return i

        