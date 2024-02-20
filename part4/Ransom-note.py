class Solution:
    def canConstruct(self, ransomNote , magazine):
      list1 = [ransomNote[i] for i in range(len(ransomNote))]
      list2 = [magazine[i] for i in range(len(magazine))]
      print(list1 , list2)
      for item in list1:
        if item in list2:
          list2.remove(item)
        else:
          return False
      return True

test = Solution()
print(test.canConstruct("aa" , "aab"))