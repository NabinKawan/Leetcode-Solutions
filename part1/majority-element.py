class Solution(object):
    def majorityElement(self, nums):
      my_dict = {}
      for item in nums:
        if item in my_dict:
          my_dict[item] += 1
        else:
          my_dict[item] = 1

      sorted_dict = sorted(my_dict.items() , key=lambda x:x[1])
      sorted_dict.reverse()

      return sorted_dict[0][0]


test = Solution()
test.majorityElement([1,2,3,4,1,1])

