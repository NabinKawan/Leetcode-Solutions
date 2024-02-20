class Solution(object):
    def checkRecord(self, s):
        in_streak = False
        attend_dict = {
          'A' : 0,
          'P' : 0,
          'L' : 0,
        }
        for i in range(len(s)):
           attend_dict[s[i]] += 1
        
        for i in range(len(s)):
          if s[i] == 'L':
            streak = 1
            while i+1 < len(s) and s[i] == s[i+1]:
              streak += 1
              if streak == 3:
                in_streak = True      
                break 
        
        if attend_dict['A'] < 2 and attend_dict['L'] <= 3 and in_streak == False:
          return True
        else:
          return False


test = Solution()
test.checkRecord("PPALLP")
print(test.checkRecord("PPALLL"))
print(test.checkRecord("LALL"))