class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hash table storing the frequency of all items in the list 
        # Then take the keys with the highest number associated for k elements 

        freq_dict = {}

        for i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1

        # used heapq which is implementation of the priority queue algorithm
        top_k = heapq.nlargest(k, freq_dict.items(), key = lambda item: item[1]) # output format [[1,3],[2,2]]
        return [item[0] for item in top_k] # Take only the first element in sub lists