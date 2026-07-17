class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        k = len(s1)
        freq1 = [0] * 26
        freq2 = [0] * 26
        base = ord('a')
        for i in range(len(s1)):
            freq1[ord(s1[i]) - base] += 1
            freq2[ord(s2[i]) - base] += 1

        if freq1 == freq2: return True
        curr = k
        while curr < len(s2):
            start = curr - k
            freq2[ord(s2[start]) - base] -= 1
            freq2[ord(s2[curr]) - base] += 1
            if freq1 == freq2: return True
            curr += 1
        
        return False