class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        nums1 = sorted(nums)
        output = []
        for i in range(len(nums1) - 1):
            j = i + 1
            k = len(nums1) - 1
            while j < k:
                if nums1[i] + nums1[j] + nums1[k] == 0:
                    if [nums1[i], nums1[j], nums1[k]] not in output:
                        output.append([nums1[i], nums1[j], nums1[k]])
                    j = j + 1
                elif nums1[i] + nums1[j] + nums1[k] < 0:
                    j = j + 1
                elif nums1[i] + nums1[j] + nums1[k] > 0:
                    k = k - 1
        return output



        

        