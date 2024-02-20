class Solution:
    def thirdMax(self, nums):
        new_list = set(nums)
        new_list = list(reversed(sorted(new_list)))
        try : 
            return new_list[2]
        except:
            return new_list[0]

test = Solution()
print(test.thirdMax([3,2,1]))
print(test.thirdMax([1,2]))