class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(0,i):
                if nums[j] == nums[i]:
                    nums.append(nums[j])
                    nums.pop(j)
        final = len(set(nums))
        return final

test1 = Solution()
test1.removeDuplicates([1,2,1,1,5])