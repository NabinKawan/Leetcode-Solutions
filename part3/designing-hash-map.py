class MyHashMap:

    def __init__(self):
      self.map = []
        

    def put(self, key: int, value: int) -> None:
       index = self.find_index(key)
       if index is not None:
        self.map[index][1] = value
       else:
        self.map.append([key , value])
        

    def get(self, key: int) -> int:
      index = self.find_index(key)
      if index is not None:
        return self.map[index][1]
      else:
        return -1
        

    def remove(self, key: int) -> None:
      index = self.find_index(key)
      if index is not None:
        self.map.pop(index)    

    def find_index(self , key):
      for i in range(len(self.map)):
        if key == self.map[i][0]:
          return i
      return None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)