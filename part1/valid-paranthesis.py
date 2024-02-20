class Solution(object):
    def isValid(self, s):
        self.str = s
        str_order = [('{','}'),('[',']'),('(',')')]
        string_list = [ ]
        result_list = []
        for i in range(len(self.str)):
          string_list.append(self.str[i])
        
        for i in range(len(string_list)):
          for item in str_order:
           if string_list[i] == item[0]:
            if i == len(string_list)-1:
              pass
            else:
             if string_list[i+1] == item[1]:
               result_list.append(True)
             else:
               result_list.append(False)

        if False in result_list:
          return False
        else:
          return True


TestCase1 = Solution()
print(TestCase1.isValid("()"))
print(TestCase1.isValid("()[]{}"))
print(TestCase1.isValid("(])"))
print(TestCase1.isValid("(}"))



        
