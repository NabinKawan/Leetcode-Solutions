class Solution:
    def minDeletionSize(self, strs) -> int:
      unsorted_coloums = 0
      tmp_li = []
      for i in range(len(strs[0])):
        new_li = []
        for j in range(len(strs)):
          new_li.append(strs[j][i])
        tmp_li.append(new_li)
      for item in tmp_li:
        if sorted(item) != item:
          unsorted_coloums += 1
      return unsorted_coloums
        

test = Solution()
print(test.minDeletionSize(["abc", "bce", "cae"]))
print(test.minDeletionSize(["cba","daf","ghi"]))
print(test.minDeletionSize(["a","b"]))
        