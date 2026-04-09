class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit condition
        if len(s) != len(t):
            return False

        dict_chars = {}
        for index in range(len(s)):
            # Increment count for character in s
            dict_chars[s[index]] = dict_chars.get(s[index], 0) + 1
            # Decrement count for character in t
            dict_chars[t[index]] = dict_chars.get(t[index], 0) - 1

        # Check if all counts are 0
        for count in dict_chars.values():
            if count != 0:
                return False

        return True
