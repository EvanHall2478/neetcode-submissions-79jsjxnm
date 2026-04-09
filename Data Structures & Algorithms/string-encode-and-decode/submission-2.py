class Solution:
    # Encodes based off length of the string and a distinguishing charactrer '#'
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0 

        while i <len(s):
            j = i
            while s[j] != '#':
                j += 1
            length_str = int(s[i:j])
            i = j + 1
            j = i + length_str
            decoded_str.append(s[i:j])
            i = j

        return decoded_str
