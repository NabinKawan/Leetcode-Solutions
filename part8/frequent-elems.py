class Solution:
    def topKFrequent(self, nums , k):
        tmp_dict = {}
        for num in nums:
            if num in tmp_dict:
                tmp_dict[num] += 1
            else:
                tmp_dict[num] = 1
        tmp_list = list(sorted(tmp_dict.items() , key =   lambda x : x[1]))
        final = []
        tmp_list.reverse()
        for i in range(k):
          final.append(tmp_list[i][0])
        return final



  

test = Solution()
print(test.topKFrequent([1,1,1,2,2,3] , 2))
print(test.topKFrequent([-1,-1] , 1))