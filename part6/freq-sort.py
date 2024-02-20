class Solution:
    def frequencySort(self, s: str) -> str:
      if s  == "":
        return ""
      self.dict = {}
      self.result = ""
      for i in range(len(s)):
        if s[i] in self.dict:
          self.dict[s[i]] += 1
        else:
          self.dict[s[i]] = 1
      
      self.list = {k:v for k , v in reversed(sorted(self.dict.items() , key = lambda item: item[1]))}
      for key , value in self.list.items():
        print(key , value)
        self.result += key * value
      return self.result

test = Solution()
test.frequencySort("tree")

