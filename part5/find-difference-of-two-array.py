class Solution:
    def findDifference(self, nums1 , nums2):
      nums1 = set(nums1)
      nums2 = set(nums2)
      return [[i for i in nums1.difference(nums2)],[i for i in nums2.difference(nums1)]]        