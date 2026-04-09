class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1

        if len(set(s)) == 1:
            return 1
        elif len(s) == 0:
            return 0

        seen = [s[l]]
        maxLen = 1

        while r < len(s):
            if s[r] not in seen:
                seen.append(s[r])
                maxLen = max(maxLen, len(seen))
                r += 1
            else:
                l += 1
                r = l + 1
                seen = [s[l]]
        return maxLen