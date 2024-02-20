class Solution(object):
    def intersect(self, nums1, nums2):
        num3 = []
        for item in nums1:
          if item in nums2:
            num3.append(item)
            nums2.remove(item)
        return num3