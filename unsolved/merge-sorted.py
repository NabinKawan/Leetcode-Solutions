class Solution(object):
    def merge(self, nums1, m, nums2, n):
        list1 = [nums1[i] for i in range(m)]
        list2 = nums2
        final_list = list1 + list2
        nums1 = sorted(final_list)

test = Solution()
test.merge([1,2,3,0,0,0],3,[2,5,6],3)
        