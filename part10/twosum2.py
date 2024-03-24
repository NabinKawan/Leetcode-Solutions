class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = 1
        while True:
            if numbers[i] + numbers[j] == target:
                return [i+1 , j+1]
            elif numbers[i] + numbers[j] > target:
                for k in range(i):
                    if numbers[k] + numbers[j] == target:
                        return[k+1 , j+1]
            i += 1
            j += 1
