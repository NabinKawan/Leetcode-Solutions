class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        self.map = {}
        if len(s) != len(t) :
          return False
        for i in range(len(s)):
          if s[i] in self.map:
            if self.map[s[i]] == t[i]:
              pass
            else:
              return False
          else:
             target_val = self._check_if_value_already_exists_(t[i])
             if target_val != True:
              self.map[s[i]] = t[i]
             else:
              return False
        print(self.map)
        return True
    
    def _check_if_value_already_exists_(self, nval):
      for key , value in self.map.items():
        if value == nval:
          return True
      return False


test = Solution()
print(test.isIsomorphic("badc","baba"))