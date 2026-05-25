class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = dict()
        for w in strs:
            k = "".join(sorted(w))
            if k in hash:
                hash[k].append(w)
            else:
                hash[k] = [w]

        return list(hash.values())