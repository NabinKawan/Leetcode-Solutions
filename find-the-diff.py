class Solution(object):
    def findTheDifference(self, s, t):
      list1 = [s[i] for i in range(len(s))]
      list2 = [t[i] for i in range(len(t))]
      list1.sort()
      list2.sort()
      for i in range(len(s)):
        if list1[i] != list2[i]:
          return list2[i]
      return list2[-1]
