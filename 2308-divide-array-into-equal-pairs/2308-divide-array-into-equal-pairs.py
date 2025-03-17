class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c=Counter(nums)
        return all(val%2==0 for val in c.values())
