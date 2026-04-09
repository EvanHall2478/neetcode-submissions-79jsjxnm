class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = collections.defaultdict(list)

        for w in strs:
            key = "".join(sorted(w))
            hashmap[key].append(w)
        return list(hashmap.values())