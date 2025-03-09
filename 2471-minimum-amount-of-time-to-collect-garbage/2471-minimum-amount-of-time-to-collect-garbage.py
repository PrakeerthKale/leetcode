from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_time = 0
        last_index = {'M': -1, 'P': -1, 'G': -1}
        
        # Calculate total collection time and last index for each type
        for i, g in enumerate(garbage):
            total_time += len(g)
            for c in g:
                last_index[c] = i
        
        # Calculate travel time
        travel_time = 0
        for c in 'MPG':
            if last_index[c] != -1:
                travel_time += sum(travel[:last_index[c]])
        
        return total_time + travel_time