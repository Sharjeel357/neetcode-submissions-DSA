

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for s in range(len(nums) - 2):

            # Optimization: once nums[s] is positive, sum can't be 0
            if nums[s] > 0:
                break

            # Skip duplicate first elements
            if s > 0 and nums[s] == nums[s - 1]:
                continue

            l = s + 1
            r = len(nums) - 1

            while l < r:

                total = nums[s] + nums[l] + nums[r]

                if total < 0:
                    l += 1

                elif total > 0:
                    r -= 1

                else:
                    result.append([nums[s], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate right values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return result