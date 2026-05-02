class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        window = []

        for char in s:
            if char not in window:
                window.append(char)
                max_length = max(max_length, len(window))
            else:
                while char in window:
                    window.pop(0)
                window.append(char)

        return max_length