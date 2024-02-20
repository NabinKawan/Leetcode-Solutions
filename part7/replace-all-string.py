class Solution:
    def replaceDigits(self, s: str) -> str:
        strlist = [ s[i] for i in range(len(s))]
        resukt_str = ""
        for i in range(len(strlist)):
          try:
            num1 = int(strlist[i])
            num2 = ord(strlist[i-1])
            strlist[i] = chr(num1+num2)
          except:
            pass
        for i in strlist:
          resukt_str += i
        return resukt_str

test = Solution()
test.replaceDigits("a1c1e1")