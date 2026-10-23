class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1

        for i in range(len(t)):
            if t[i] in map:
                map[t[i]] -= 1
            else:
                map[t[i]] = 1

        for i in range(len(s)):
            if map[s[i]] != 0:
                return False
        
        return True
        