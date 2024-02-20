class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.split()
        return len(word[-1])

test = Solution()
print(test.lengthOfLastWord("hell world"))