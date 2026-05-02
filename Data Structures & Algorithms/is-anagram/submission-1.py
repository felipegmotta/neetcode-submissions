class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_chars_s = {}
        dict_chars_t = {}
        for idx in range(len(s)):
            dict_chars_s[s[idx]] = 1 if dict_chars_s.get(s[idx]) is None else dict_chars_s[s[idx]] + 1
            dict_chars_t[t[idx]] = 1 if dict_chars_t.get(t[idx]) is None else dict_chars_t[t[idx]] + 1 

        print(dict_chars_s)
        print(dict_chars_t)
        return dict_chars_s == dict_chars_t