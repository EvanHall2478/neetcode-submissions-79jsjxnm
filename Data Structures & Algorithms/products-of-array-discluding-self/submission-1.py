class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        # The product except self is the prefix multiplied by the postfix 

        # Calculate the prefix in place and store within the output
        prefix = 1
        # forwards pass to get the prefixes
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        # Calculate the postfix in place and store within the output
        postfix = 1
        # backwards pass to get the postfixes
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output