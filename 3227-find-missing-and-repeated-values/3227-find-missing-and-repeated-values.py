from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Flatten the 2D list into a single list
        flattened_list = [num for sublist in grid for num in sublist]
        count = {}
        repeated = -1
        missing = -1

        # Count occurrences and find the repeated value
        for num in flattened_list:
            if num in count:
                repeated = num
            else:
                count[num] = 1

        # Find the missing value
        current = 1
        while True:
            if current not in count:
                missing = current
                break
            current += 1

        return [repeated, missing]
