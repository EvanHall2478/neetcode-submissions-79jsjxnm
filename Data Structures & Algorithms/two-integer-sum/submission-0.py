class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store possible solutions
        num_dict = {}

        # Iteate through the list of numbers tracking the index
        for i in range(len(nums)):
            complement = target - nums[i] # Find the complement of the current number to the target

            # If the complement is in the dictionary then you have your one solution to the problem
            if complement in num_dict:
                return [num_dict[complement], i]
            
            num_dict[nums[i]] = i # If the complement is not in the dictionary then add the current number and continue iterating
        return [] # If no solution is found return an empty list