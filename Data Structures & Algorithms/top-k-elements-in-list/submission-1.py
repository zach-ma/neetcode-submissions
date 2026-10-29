class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            if n not in hm:
                hm[n] = 1
            else:
                hm[n] = hm[n] + 1
        sorted_hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_hm.keys())[:k]
