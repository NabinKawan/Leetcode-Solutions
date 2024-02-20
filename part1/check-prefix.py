class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        sentence_list = sentence.split()
        for i in range(len(sentence_list)):
          if sentence_list[i].startswith(searchWord):
            return i+1
        return -1
        