class Solution(object):
    def findLUSlength(self, a, b):
      list1 = []
      for i in range(len(a)):
          for j in range(i+1 , len(a)):
            print(a[i:j])
            if a[i:j] not in b:
               list1.append(len(a[i:j])+1)
      
      list1.sort()
      return list1[-1]

test = Solution()
test.findLUSlength("aba","cdc")