class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        mLen = 0
        l,r = 0,0
        while r < len(s):
            if s[r] not in visited:
                visited.add(s[r])
                mLen = max(mLen,r-l+1)
                r+=1
            else:
                while s[r] in visited:
                    visited.remove(s[l])
                    l+=1
        return mLen
