class Solution:
    def longestConsecutive(self, nums):
        new_list = list(set(nums))
        max_seq = 0
        current_seq = 1
        new_list.sort()
        print(new_list)
        if len(new_list) == 1:
          return 1
        for i in range(len(new_list)-1):
          if new_list[i+1] - new_list[i] == 1:
            current_seq += 1
          else:
            current_seq = 1
          if current_seq > max_seq:
            max_seq = current_seq
        return max_seq


test = Solution()
print(test.longestConsecutive([1]))
print(test.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(test.longestConsecutive([1,2,0,1]))