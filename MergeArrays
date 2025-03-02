class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        id_values = {}
        
        for id, value in nums1 + nums2:
            if id in id_values:
                id_values[id] += value
            else:
                id_values[id] = value
        
        return sorted([[id, value] for id, value in id_values.items()])
