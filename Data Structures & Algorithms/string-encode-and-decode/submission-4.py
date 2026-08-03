class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        encoded_string = "~".join(strs)
        encoded_string += "~"
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        l = 0
        for i in range(len(s)):
            if s[i] == "~" or i == len(s):
                decoded_string.append(s[l:i])
                l = i + 1
        return decoded_string