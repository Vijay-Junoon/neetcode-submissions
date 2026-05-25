class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for wrd in range(len(strs)):
            s1 = "".join(sorted(list(strs[wrd])))
            if s1 in res.keys():
                res[s1].append(strs[wrd])
            else:
                res[s1] = [strs[wrd]]
        return(list(res.values()))