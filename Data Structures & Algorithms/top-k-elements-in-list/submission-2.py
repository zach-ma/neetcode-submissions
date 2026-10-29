class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''my soln: sorting + hash map
        T: O(nlogn)
        lesson: too slow, can be done in O(n)
        '''
        # hm = {}
        # for n in nums:
        #     if n not in hm:
        #         hm[n] = 1
        #     else:
        #         hm[n] = hm[n] + 1
        # sorted_hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))
        # return list(sorted_hm.keys())[:k]

        '''neet
        '''
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0) # NOTE: default
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            if len(res) >= k:
                return res[:k]
            if freq[i]:
                res += freq[i]
        










