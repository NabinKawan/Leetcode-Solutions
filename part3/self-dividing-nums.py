class Solution(object):
    def selfDividingNumbers(self, left, right):
       list = [ ]
       for i in range(left  ,right+1):
        status = True
        num = str(i)
        if '0' in num:
          pass
        else:
         for j in range(len(num)):
          if  i% int(num[j]) != 0 :
            status = False
            break
         if status:
          list.append(i)
       return list
  
test = Solution()
test.selfDividingNumbers(47,85)

