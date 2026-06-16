class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1

        while l < r:
            step = numbers[l] + numbers[r]
            if step == target:
                return [l + 1, r + 1]
            elif step > target:
                r -= 1
            else:
                l += 1
        
         