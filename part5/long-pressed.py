class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        return len(name) != len(typed)