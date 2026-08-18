class Solution:
    def isPalindrome(self, s: str) -> bool:
        striped_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # print(striped_s)
        
        for i in range(len(striped_s) // 2):
            if striped_s[i] != striped_s[-i-1]:
                # print(striped_s[i], striped_s[-i-1])
                return False
        return True