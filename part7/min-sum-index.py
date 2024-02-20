class Solution:
    def findRestaurant(self, list1 , list2):
      common_list = []
      min_sum = None
      for i in range(len(list1)):
        if list1[i] in list2:
          j = list2.index(list1[i])
          sum = i + j 
          common_list.append([list1[i] , sum])
          if min_sum is None or min_sum > sum:
            min_sum == sum
      if len(common_list) == 0:
        return None
      new_list = [item[0] for item in common_list if item[1] == min_sum]
      return new_list

test = Solution()
test.findRestaurant( ["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])