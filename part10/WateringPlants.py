class Solution(object):
    def wateringPlants(self, plants, capacity):
        self.steps_taken = 0
        current_water = capacity
        
        for i in range(len(plants)):
            if current_water < plants[i]:
                self.steps_taken += (( i+1 ) * 2 ) - 1
                current_water = capacity
            else:
                self.steps_taken  += 1
            current_water -= plants[i]
        
        return self.steps_taken
