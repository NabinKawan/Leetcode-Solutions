class WordDictionary:

    def __init__(self):
        self.list = []

    def addWord(self, word: str) -> None:
        self.list.append(word)

    def search(self, word: str) -> bool:
      word = word.replace("." , "")
      if word in self.list:
        return True
      for added_word in self.list:
        if word in added_word:
          return True
      return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)