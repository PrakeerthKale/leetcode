class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sums = []
        left, right = 0, len(nums) - 1
        while left < right:
            pair_sums.append(nums[left] + nums[right])
            left += 1
            right -= 1
        return max(pair_sums)

