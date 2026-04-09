class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(1) early exit condition
        if len(s) != len(t):
            return False
        
        # O(n) createa a hash table to store the number of all letter in strings
        count = defaultdict(int) # from collections

        # O(n) iterate through both strings
        for i in s:
            count[i] += 1
        for j in t:
            count[j] -= 1
        
        # O(1) check if all values in the hash table are 0
        for freq in count.values():
            if freq != 0:
                return False
        return True