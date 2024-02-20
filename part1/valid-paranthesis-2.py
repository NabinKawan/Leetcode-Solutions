class Solution(object):
  def isValid(self , s):
    self.user_string = [i for i in s]
    valid_string_format = [('{','}'),('[',']'),('(',')')]
    cases_result = []
    self.nested = "Not-Nested"
    starting_string = self.user_string[0]
    end_string = self.user_string[-1]

    #test case 1 check of the number of string list is even
    is_even_string = len(self.user_string)%2 == 0
    if is_even_string != True: return False

    #test if the string characters are serperated or nested
    for item in valid_string_format:
      if item[0] == starting_string and item[1] == end_string:
        self.nested = "Nested"

    if self.nested == "Not-Nested" or len(self.user_string) == 2:
      for i in range(len(self.user_string)):
        if i == len(self.user_string)-1:
          pass
        else:
          for item in valid_string_format:
            if item[0] == self.user_string[i]:
              if item[1] == self.user_string[i+1]:
                cases_result.append(True)
              else:
                cases_result.append(False)
      if False in cases_result or cases_result == [] or len(cases_result) != len(self.user_string)/2:
        return False
      else:
        return True
    
    #if nested runs the nested checker using the first item and the last item and so on
    elif self.nested == "Nested":
      for i in range(len(self.user_string)//2):
        item = (self.user_string[i],self.user_string[-1-i])
        if item in valid_string_format:
          cases_result.append(True)
        else:
          cases_result.append(False)
    
    #checks if there is a false case in any of the case and returns the result
    if False in cases_result:
      return False
    else:
      return True


    
    


TestCase1 = Solution()
print(TestCase1.isValid("()"))#true
print(TestCase1.isValid("()[]{}"))#true
print(TestCase1.isValid("(])"))#false
print(TestCase1.isValid("{[]}"))#true
print(TestCase1.isValid("{(({[]}))}"))#true
print(TestCase1.isValid("{([)}"))#false
print(TestCase1.isValid("{(}"))#false
print(TestCase1.isValid("){"))#false


        
