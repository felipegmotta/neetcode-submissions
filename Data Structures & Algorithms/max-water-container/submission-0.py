class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0
        left = 0
        right = len(heights) - 1
        for idx, height in enumerate(heights):
            distance = right - left
            current_area = distance * min(heights[left], heights[right])

            if current_area > max_area:
                max_area = current_area

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            
        return max_area