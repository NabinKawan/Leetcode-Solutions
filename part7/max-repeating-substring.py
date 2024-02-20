class Solution:
    def maxRepeating(self, sequence: str, word: str):
      count = 0
      while word in sequence:
        sequence = sequence.replace(word , "
        
        
        ",1)
        count += 1
      print(count)
      return count

test = Solution()
test.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba","aaaba ")