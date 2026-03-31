class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)-1): 
            for j in range(len(nums)):
                if j > i and nums[i] + nums[j] == target:
                    a.append(i)
                    a.append(j)
                else:
                    j = j + 1
        return a