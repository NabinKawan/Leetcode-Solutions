class Solution(object):
    def numOfPairs(self, nums, target):
        self.target = target
        self.result = 0
        self.nums = nums
        for i in range(len(nums)):
            self.traverse(i , 0)
        
        return self.result
    

    def traverse(self , i , j):
        if i != j and self.nums[i] + self.nums[j] == self.target:
            self.result +=1
        if j < len(self.nums)-1:
            self.traverse(i , j+1)
