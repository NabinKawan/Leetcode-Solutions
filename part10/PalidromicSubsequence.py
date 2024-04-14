class Solution(object):
    def removePalindromeSub(self, s):
        
        if len(s) == 0:
            return 0
        else:
            if s == s[::-1]:
                return 1
            else:
                return 2
