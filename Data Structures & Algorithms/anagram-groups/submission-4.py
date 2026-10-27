class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''my soln: sorting
        '''
        # groups = {}
        # for s in strs:
        #     sorted_s = "".join(sorted(s))
        #     if sorted_s not in groups:
        #         groups[sorted_s] = []
        #     groups[sorted_s].append(s)
        # return list(groups.values()) # NOTE: need to convert dynamic view to list explicitly
        '''neet 1: sorting
        '''
        # res = defaultdict(list) # NOTE: create dict with default value as []
        # for s in strs:
        #     sortedS = "".join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())

        '''neet 2: hash table (using fixed length tuples as key)!!!!!
        '''
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # fixed length
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # NOTE: use tuple as hash key!!!!
        return list(res.values())


