class Solution:
    def checkStraightLine(self, coordinates):
      y = coordinates[1][1] - coordinates[0][1]
      x = coordinates[1][0] - coordinates[0][0]
      try:
       slope = y/x
      except:
        slope = None
      for cor in coordinates[1::]:
        y = cor[1] - coordinates[0][1]
        x = cor[0] - coordinates[0][0]
        try : 
         demo_slpoe = y/x
        except:
          demo_slpoe = None
        if demo_slpoe != slope:
          return False
      return True

test = Solution()
#print(test.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
#print(test.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
print(test.checkStraightLine([[0,0],[0,1],[0,-1]]))