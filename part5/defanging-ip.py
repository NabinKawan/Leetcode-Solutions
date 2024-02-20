class Solution:
    def defangIPaddr(self, address: str):
      final = address.replace('.' ,'[.]')
      return final