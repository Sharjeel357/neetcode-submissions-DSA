from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Count frequencies
        freq = Counter(nums)

        # Get top k frequent elements
        return [num for num, count in freq.most_common(k)]