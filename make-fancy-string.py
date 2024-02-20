class Solution:
    def makeFancyString(self, s: str) -> str:
        self.list = []
        result = ''
        for i in range(len(s)):
          if len(self.list) < 2:
            self.list.append(s[i])
          else:
            self._compare_to_stack_(s[i])
        for item in self.list:
          result += item
        return result
    
    def _compare_to_stack_(self , item):
      if self.list[-1] == item and self.list[-1] == self.list[-2]:
        pass
      else:
        self.list.append(item)

test = Solution()
test.makeFancyString("leeetcode")