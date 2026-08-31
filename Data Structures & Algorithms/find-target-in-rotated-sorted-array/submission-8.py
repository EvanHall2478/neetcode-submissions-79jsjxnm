class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1


        while left <= right:
            mid = (left + right) // 2
            # print(nums[left], nums[mid], nums[right])
            
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
                    

            # elif target < nums[mid] and target > nums[right] or \
            # target > nums[mid] and target > nums[right]:
            #     right = mid - 1

            # elif target < nums[mid] and target < nums[right] or \
            # target > nums[mid] and target < nums[right]:
            #     left = mid + 1

           
            # else:
            #     return right
        return -1