class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = {}
        l,r = 0,0
        mLen,mVal = 0,0
        while r < len(s):
            hash[s[r]] = hash.get(s[r],0) + 1
            mVal = max(mVal,hash[s[r]])
            length = r - l + 1
            if length - mVal <= k:
                mLen = max(mLen,length)
            else:
                hash[s[l]] -= 1
                if hash[s[l]] == 0: del hash[s[l]]
                l+=1
            r+=1
        return mLen