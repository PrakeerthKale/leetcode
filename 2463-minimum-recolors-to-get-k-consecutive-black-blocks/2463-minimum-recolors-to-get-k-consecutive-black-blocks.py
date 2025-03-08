class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_rec = float('inf')
        white_count = 0

        # Count the number of whites in the first window
        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1

        min_rec = min(min_rec, white_count)

        # Slide the window to the right
        for i in range(k, n):
            if blocks[i - k] == 'W':
                white_count -= 1
            if blocks[i] == 'W':
                white_count += 1
            min_rec = min(min_rec, white_count)

        return min_rec
