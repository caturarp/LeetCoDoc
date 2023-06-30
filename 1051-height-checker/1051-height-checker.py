class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len([i for i in range(0, len(heights)) if heights[i] != sorted(heights)[i]])