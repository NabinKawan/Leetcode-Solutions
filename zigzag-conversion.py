class Solution:

  def Convert(self , txt , rows):
    table = [[] for i in range(rows)]
    
    row = 0
    direction = -1

    if rows == 1:
      return txt 

    for j in txt:
      table[row].append(j)
      if row == 0 or row == len(table)-1:
        direction *= -1
      row += direction 
    
    result = ""
    for row in table:
      for elem in row:
        result += elem 
    
    return result 
