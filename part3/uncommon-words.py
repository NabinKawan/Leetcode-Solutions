class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        s1 = set(s1.split())
        s2 = set(s2.split())
        return s1.symmetric_difference(s2)

test = Solution()
print(test.uncommonFromSentences( "this apple is sweet","this apple is sour"))