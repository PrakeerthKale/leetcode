class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index = word.find(ch)
        if index != -1:
            prefix = word[:index + 1]
            suffix = word[index + 1:]
            return prefix[::-1] + suffix
        return word
