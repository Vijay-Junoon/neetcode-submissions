class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        j = 0
        for j in range(len(strs[0])):
            for i in range(1,len(strs)):
                
                if j == len(strs[i]) or not strs[i] or strs[i][j] != strs[0][j]:
                    return prefix
            
            prefix += strs[0][j]

        return prefix