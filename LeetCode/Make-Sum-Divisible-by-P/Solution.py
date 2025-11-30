class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        rem = sum(nums)%p
        if rem == 0:
            return 0
        last = {0: -1}
        curr = 0
        n = len(nums)
        for i, x in enumerate(nums):
            curr = (curr+x)%p
            nxt = (curr-rem+p)%p
            if nxt in last:
                n = min(n, i - last[nxt])
            last[curr] = i
        return -1 if n == len(nums) else n