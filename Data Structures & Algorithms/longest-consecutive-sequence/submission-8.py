class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        result = 0

        for i in num_set:
            if i - 1 not in num_set:
                temp = i
                count = 0
                while temp in num_set:
                    count += 1
                    temp += 1
                result = max(result, count)
        return result