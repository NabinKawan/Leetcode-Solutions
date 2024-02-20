class Solution:
    def destCity(self, paths):
      first_city = paths[0][0]
      final_city = paths[0][1]
      if paths == []:
        return None
      for item in paths:
        for item in paths:
          if item[1] == final_city:
            final_city = item[0][1]
      return final_city

test = Solution()
print(test.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
