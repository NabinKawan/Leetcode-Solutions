class Solution(object):
    def customSortString(self, order, s):
        final_str = ""
        for i in range(len(order)):
            while order[i] in s:
                s = s.replace(order[i] , "" , 1)
                final_str += order[i]
        return final_str + s
