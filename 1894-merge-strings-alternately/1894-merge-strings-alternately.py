class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = ""  # Use a string to store the merged characters
        l1 = len(word1)
        l2 = len(word2)
        i = 0

        # Use a while loop to merge characters alternately
        while i < l1 and i < l2:
            m += word1[i]
            m += word2[i]
            i += 1
        while i < l1:
            m += word1[i]
            i += 1
        while i < l2:
            m += word2[i]
            i += 1
        return m