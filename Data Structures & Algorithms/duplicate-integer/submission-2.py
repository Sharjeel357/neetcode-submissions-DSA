class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        result = False
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                result = True
                break
        
            else:
                result = False
        
        return result