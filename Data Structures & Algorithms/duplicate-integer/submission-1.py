# Time Complexity: O(n) -> set() is O(n) and len() is O(1)
# Space Complexity: O(n) -> set() is O(n)
# However can exit early as soon as a duplicate is found
class Solution:
    def hasDuplicate(self, nums: list[int])->bool:
        if len(nums) == len(set(nums)):
            return False
        return True
