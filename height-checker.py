class Solution(object):
    def heightChecker(self, heights):
        list1 = heights
        list2 = sorted(heights)
        out_of_index = 0
        for i in range(len(list1)):
          if list1[i] != list2[i]:
            out_of_index += 1
        return out_of_index


test = Solution()
print(test.heightChecker([1,1,4,2,1,3]))
print(test.heightChecker([5,1,2,3,4]))