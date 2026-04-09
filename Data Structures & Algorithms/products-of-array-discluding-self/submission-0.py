# With division operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        product = 1
        number_zeros = 0
        

        # Get the product of all of the numbers in the list
        for num in nums:
            if num == 0:
                number_zeros += 1

                # More than two zeros in nums. Therefore all are zero
                if number_zeros > 1:
                    return output
                product = product

            else:
                product *= num


        for i in range(len(nums)):
            # If there is a single zero than all other indices are 0
            if number_zeros:
                if nums[i] == 0:
                    output[i] = int(product)
                else:
                    continue
            else:
                output[i] = int(product / nums[i])
        return output



        
