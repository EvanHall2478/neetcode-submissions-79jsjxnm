class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        # Iterate throught he lsit of strings
        for s in strs:
            key = ''.join(sorted(s)) # create a key of the sorted string which other sorted strings can be compared to to group anagrams
            # Cehck if the key is in the dictionary and if not initialize
            if key in dict:
                dict[key].append(s)
            else:
                dict[key] = [s]
        return list(dict.values()) # Returns the values associated under the keys formated as a list of lists 