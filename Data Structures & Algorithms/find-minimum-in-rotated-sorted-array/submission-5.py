class Solution:
    def findMin(self, nums: List[int]) -> int:
        # case where sorted %n times return nums[0]
        if len(nums) == 1:
            return nums[0]
        # if len(nums) == 2:
        #     return min(nums)

        left = 0
        right = len(nums) - 1
        # implement binary search 
        while left <= right:
            mid = (left + right) // 2
            print(nums[left], nums[mid], nums[right])

            if  nums[mid] < nums[right] and nums[mid] < nums[left]:
                right -= 1
                left += 1
            elif (nums[left] <  nums[mid] or nums[left] == nums[mid]) \
            and nums[left] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        
        return nums[mid]

        
        