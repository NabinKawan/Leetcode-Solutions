class Solution:
    def removeDuplicates(self, s: str) -> str:
        self.list = []
        final_str = ''
        for i in range(len(s)):
          if len(self.list) == 0 :
            self.list.append(s[i])
          else:
            self._append_to_stack_(s[i])
        
        for item in self.list:
          final_str += item
        return final_str
    
    def _append_to_stack_(self , item):
      if self.list[-1] == item:
        self.list.pop(-1)
      else:
        self.list.append(item)
  

test = Solution()
print(test.removeDuplicates("abbaca"))