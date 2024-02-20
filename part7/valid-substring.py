class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = None
        if s == "":
            return 0
        elif s == " ":
            return 1
        for i in range(len(s)):
            for j in range(i , len(s)+1):
                seq = s[i:j]
                valid = self._is_valid_substring(seq)
                if valid:
                    if longest_substring == None or len(longest_substring) < len(seq):
                        longest_substring = seq
        return len(longest_substring)

    def _is_valid_substring(self, seq):
        seq_list = []
        for i in range(len(seq)):
            if seq[i] not in seq_list:
                seq_list.append(seq[i])
            else:
                return False
        return True
        
test = Solution()
print(test.lengthOfLongestSubstring("c"))