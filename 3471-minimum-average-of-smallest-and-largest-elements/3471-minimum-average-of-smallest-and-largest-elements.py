class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        averages = []
        
        for i in range(n // 2):
            minElement = nums[i]
            maxElement = nums[n - i - 1]
            averages.append((minElement + maxElement) / 2.0)
        
        return min(averages)

