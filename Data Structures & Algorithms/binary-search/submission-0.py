class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        for i in nums:
            if target in nums:
                if nums[mid] < target:
                    mid+=1
                elif nums[mid] > target:
                    mid-=1
                elif nums[mid] == target:
                    return mid
            else:
                return -1