class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        current = s + "X"

        freq_t = {}
        for char in t:
            freq_t[char] = 1 + freq_t.get(char, 0)

        l = 0
        for r in range(len(s)):

            if s[r] in freq_t.keys():
                freq_t[s[r]] -= 1

            while max(freq_t.values()) == 0:
                if len(s[l:r + 1]) < len(current):
                    current = s[l:r + 1]

                if s[l] in freq_t.keys():
                    freq_t[s[l]] += 1
                
                l += 1 
        
        if current != s + "X":
            return current
        return res

