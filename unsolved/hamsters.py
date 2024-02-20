class Solution(object):
    def minimumBuckets(self, hamsters):
      self.list = []
      self.food = 0
      for i in range(len(hamsters)):
        if hamsters[i] == 'h':
          pass

Test = Solution()
Test.minimumBuckets("H..H") # should return 2
Test.minimumBuckets(".H.H.") #should return 1
Test.minimumBuckets(".HHH.") #should return -1

