class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key in hash:
                hash[key].append(word)
            else:
                hash[key] = [word]
        
        return list(hash.values())