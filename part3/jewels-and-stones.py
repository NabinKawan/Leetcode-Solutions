class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
      jewels_dict = {}
      final_value = 0
      for i in range(len(jewels)):
        jewels_dict[jewels[i]] = 0 
      
      for i in range(len(stones)):
        if stones[i] in jewels_dict:
          jewels_dict[stones[i]] += 1
      
      print(jewels_dict)
      for value in jewels_dict.values():
        final_value += value
      
      return final_value

test = Solution()
print(test.numJewelsInStones("aA","aAAbbbb"))