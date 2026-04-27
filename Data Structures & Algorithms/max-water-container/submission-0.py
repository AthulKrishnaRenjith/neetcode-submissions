class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if j != i:
                    if (min(heights[i], heights[j]) * abs(j - i)) > mx:
                        mx = (min(heights[i], heights[j]) * abs(j - i))
        return mx