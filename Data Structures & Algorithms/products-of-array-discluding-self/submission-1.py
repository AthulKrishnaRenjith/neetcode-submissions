import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        output = []
        for i in range(len(nums)):
            left.append(math.prod(nums[:i]) if i != 0 else 1)
            right.append(math.prod(nums[i+1 : len(nums)]) if i != len(nums) - 1 else 1)
        for j in range(len(left)):
            output.append(left[j] * right[j])  
        return output
            
        