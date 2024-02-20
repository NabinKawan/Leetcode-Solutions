class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        self.list1 = []
        self.list2 = []
        for i in range(len(s)):
          if self.list1 == [] and s[i] != '#':
            self.list1.append(s[i])
          elif s[i] == '#':
            if len(self.list1) != 0:
             self.list1.pop(-1)
          else:
            self.list1.append(s[i])
        for i in range(len(t)):
          if self.list2 == [] and t[i] != '#':
            self.list2.append(t[i])
          elif t[i] == '#':
            if len(self.list2) != 0:
             self.list2.pop(-1)
          else:
            print("appending" , t[i])
            self.list2.append(t[i])
        print(self.list1 , self.list2)
        return self.list1 == self.list2

test = Solution()
print(test.backspaceCompare("y#fo##f" , "y#f#o##f"))
