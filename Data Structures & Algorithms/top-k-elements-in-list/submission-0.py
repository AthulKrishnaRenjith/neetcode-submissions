class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l: dict
        l = {}
        s = []
        i = 0
        while i < len(nums):
            if nums[i] not in l:
                l[nums[i]] = 1
            else:
                l[nums[i]] = l[nums[i]] + 1
            i = i + 1
        while len(s) != k:
            j = list (l.keys())[list (l.values()).index(max (list (l.values())))]
            s.append(j)
            l[j] = 0
        return s
        