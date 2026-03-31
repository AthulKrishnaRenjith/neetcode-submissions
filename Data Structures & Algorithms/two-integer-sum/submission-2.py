class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solved = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in solved: 
                return [solved[diff], i]
            solved[n] = i