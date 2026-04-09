class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = [0] * len(nums)
        output = []
        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                left.append(left[-1] * nums[i-1])
        j = len(nums) - 1
        while j >= 0:
            if j == len(nums) - 1:
                right[j] = 1
            else:
                right[j] = right[j+1] * nums[j + 1]
            j = j - 1
        for j in range(len(left)):
            output.append(left[j] * right[j])  
        return output
            
        