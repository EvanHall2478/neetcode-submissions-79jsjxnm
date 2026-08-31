class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # right side is the lower end of the sort
                left = mid + 1
            else:
                # right side is not the sorted end so delete
                right = mid
        return nums[left]