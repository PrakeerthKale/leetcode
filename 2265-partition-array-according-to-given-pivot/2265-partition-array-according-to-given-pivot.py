class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = [x for x in nums if x < pivot]
        equal = [x for x in nums if x == pivot]
        greater = [x for x in nums if x > pivot]
        return less + equal + greater


        