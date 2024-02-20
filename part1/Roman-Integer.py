class Solution(object):

    def __init__(self, *args, **kwargs):
        self.roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        self.roman_sub_values = [('I','V',4),('I','X',9),('X','L',40),('X','C',90),('C','D',400),('C','M',900)]
        self.intValue = 0
        self.skipNext = False
        self.insert = False

    def romanToInt(self, s):
      for i in range(len(s)):
        if self.skipNext == False:
          if i == len(s)-1:
            for key,value in self.roman_dict.items() :
              if s[i] == key:
                print(f"{value}- endloop")
                self.intValue += value
                self.insert = True
                break
          else:
            for item in self.roman_sub_values:
                if s[i] == item[0] and s[i+1] == item[1]:
                  print(f"{item[2]}--replace loop")
                  self.intValue += item[2]
                  self.skipNext = True
                  self.insert = True
                  break
            if self.insert == False:
             for key,value in self.roman_dict.items() :
              if s[i] == key:
                  print(f"{value}-- normal loop")
                  self.intValue += value
                  break
        else :
           self.skipNext = False
           self.insert = False
           continue
      return self.intValue


testCase1 = Solution()
testCase2 = Solution()
testCase3 = Solution()
testCase4 = Solution()

print(testCase1.romanToInt("MCMXCVI"))
