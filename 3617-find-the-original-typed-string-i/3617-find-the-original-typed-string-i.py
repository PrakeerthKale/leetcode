class Solution:
    def possibleStringCount(self, word: str) -> int:
        re=1
        for i in range(1,len(word)):
            if word[i-1]==word[i]:
                re+=1
        return re