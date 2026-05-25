class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        
        hash = dict()
        for i in s:
            hash[i] = hash.get(i,0) + 1

        for i in t:
            if i not in hash:
                return False
            hash[i] -= 1

        for i in s:
            if hash[i] != 0:
                return False
        return True