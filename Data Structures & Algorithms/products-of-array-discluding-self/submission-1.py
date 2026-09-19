class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # arr = [ 1 , 2 , 4 , 6]

        # result = []

        # total_product = 1

        # for i in nums:
        #     total_product = total_product * i

        # for j in range(len(nums)):
        #     result.append(total_product//nums[j])
        
        # return result

        result = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result