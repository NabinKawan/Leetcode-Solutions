class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        list1 = sorted(s1)
        list2 = sorted(s2)
       
        break1 = self.check_if_breaks(list1,list2)
        break2 = self.check_if_breaks(list2,list1)

        if break1 == True or break2 == True:
            return True
        else:
            return False


    def check_if_breaks(self , list1 , list2):
        for i in range(len(list1)):
            if ord(list1[i]) < ord(list2[i]):
                return False
        return True
