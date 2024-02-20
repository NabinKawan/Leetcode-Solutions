class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
      for i in range(n):
        nums1[m] = nums2[i]
        m += 1 
      nums1.sort()

test = Solution()
print(test.merge([1,2,3,0,0,0],3,[2,5,6],3))