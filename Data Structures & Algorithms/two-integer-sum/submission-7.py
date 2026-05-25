class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = [(num, i) for i, num in enumerate(nums)]
        indexed.sort()

        left, right = 0, len(nums) - 1

        while left < right:
            s = indexed[left][0] + indexed[right][0]

            if s == target:
                return sorted([indexed[left][1], indexed[right][1]])
            elif s < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]