class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        window = []

        for char in s:
            if char in window:
                while char in window:
                    window.pop(0)

            window.append(char)
            max_length = max(max_length, len(window))

        return max_length