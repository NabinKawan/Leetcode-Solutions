class Solution:
    def findKthLargest(self, nums , k):
        nums.sort()
        nums.reverse()
        return nums[k-1]




test = Solution()
test.findKthLargest([3,2,1,5,6,4] , 2)
test.findKthLargest( [3,2,3,1,2,4,5,5,6] , 4)