class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        b, s, m = 0, 0, 0
        for e in range(len(nums)):
            while b & nums[e]:
                b ^= nums[s]
                s += 1
            b |= nums[e]
            m = max(m, e - s + 1)
        return m
