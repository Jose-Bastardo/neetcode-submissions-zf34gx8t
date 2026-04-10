class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sLetters = sorted(list(s))
        tLetters = sorted(list(t))

        if sLetters == tLetters:
            return True
        else:
            return False
