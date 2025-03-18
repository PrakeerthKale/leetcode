class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        b = 0
        s = 0
        m = 0
        for e in range(n):
            while b & nums[e]:
                b ^= nums[s]
                s += 1
            b |= nums[e]
            m = max(m, e - s + 1)
        return m
