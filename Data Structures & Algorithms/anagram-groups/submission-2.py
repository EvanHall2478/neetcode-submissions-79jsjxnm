class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = {}
        for i in strs:
            key = tuple(sorted(i))
            if key in counters:
                counters[key].append(i)
            else:
                counters[key] = [i]  
        return list(counters.values())