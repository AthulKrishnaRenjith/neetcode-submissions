class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        multiple = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i :
                    multiple = multiple * nums[j]
            output.append(multiple)
            multiple = 1
        return output
            
        