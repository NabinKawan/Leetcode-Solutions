class Solution(object):
    def arrayRankTransform(self, arr):
      dict = {}
      i = 1
      new_list = []
      for items in sorted(arr):
        if items not in dict:
         dict[items] = i 
         i +=1
      for items in arr:
        new_list.append(dict[items])
      return new_list
      

        

Test1 = Solution()
Test1.arrayRankTransform([40,10,30,20])
Test1.arrayRankTransform([100,100,100])