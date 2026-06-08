class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        def backtrack(start,target,arr):
            if target == 0:
                res.append(arr[:])

            for i in range(start,len(candidates)):
                
                val = candidates[i]
                if i > start and val == candidates[i-1]:
                    continue

                if val > target:
                     break

                arr.append(val)
                backtrack(i+1,target-val,arr)
                arr.pop()

        backtrack(0,target,[])
        return res
                