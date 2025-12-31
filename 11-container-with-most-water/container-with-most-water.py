class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height) - 1
        out = 0

        while p1 < p2:
            area = min(height[p1], height[p2]) * (p2 - p1)
            out = max(out, area)

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return out