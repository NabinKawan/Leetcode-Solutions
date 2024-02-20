class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        max_candy = max(candies)
        result_list = []
        for kid in candies:
            if kid + extraCandies >= max_candy:
                result_list.append(True)
            else:
                result_list.append(False)
        return result_list

test = Solution()
print(test.kidsWithCandies([2,3,5,1,3], 3))
        