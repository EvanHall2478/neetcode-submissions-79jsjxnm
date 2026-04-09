# Time Complexity: O(n) -> set() is O(n) and len() is O(1)
# Space Complexity: O(n) -> set() is O(n)
# However can exit early as soon as a duplicate is found
class Solution:
    def hasDuplicate(self, nums: list[int])->bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False