class Solution:
    def wordBreak(self, s , wordDict):

      valid_list = [item for item in wordDict if item in s]
      print(valid_list)



test = Solution()
test.wordBreak("leetcode" , ["leet" , "code"])
print(test.wordBreak("aaaaaaaa" , ["aaaa" , "aaa" , "aa"]))