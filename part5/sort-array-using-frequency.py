class Solution:
    def frequencySort(self, nums):
      frequency_dict = {}
      sorted_array = []
      for num in nums:
        if num in frequency_dict:
          frequency_dict[num] += 1
        else:
          frequency_dict[num] = 1
      while len(frequency_dict) != 0:
        number = None
        frequency = None
        for key , values in frequency_dict.items():
          if number is None and frequency is None:
            number = key
            frequency = values
          elif frequency > values:
            number = key
            frequency = values
          elif frequency == values:
            if key > number:
              number = key
              frequency = values
        for i in range(frequency):
          sorted_array.append(number)
        frequency_dict.pop(number)
      return sorted_array
      
      


test = Solution()
test.frequencySort([1,1,2,2,2,3])
test.frequencySort([2,3,1,3,2])
test.frequencySort([-1,1,-6,4,5,-6,1,4,1])

        