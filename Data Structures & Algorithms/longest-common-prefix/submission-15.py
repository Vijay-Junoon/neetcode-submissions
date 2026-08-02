class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""

        for i in range(len(strs[0])):
            for word in strs[1:]:
                if  i >= len(word):break
                if word == "" or word[i] != strs[0][i]:
                    return prefix
            else:
                prefix += strs[0][i]
        return prefix