class Solution:
    def groupAnagrams(self, strs) -> list:
        # Initialize a standard dictionary
        anagram_groups = {}

        for s in strs:
    # Sort the string to create a canonical key
            sorted_s = "".join(sorted(s))
    # If the sorted key is not in the dictionary, add it with an empty list
            if sorted_s not in anagram_groups:
                anagram_groups[sorted_s] = []
    # Add the original string to the list associated with its sorted key
            anagram_groups[sorted_s].append(s)

# The result is the list of all values (which are lists of anagrams)
        output = list(anagram_groups.values())
        return output

# Test the solution
solver = Solution()
input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solver.groupAnagrams(input_strings)
print(result)