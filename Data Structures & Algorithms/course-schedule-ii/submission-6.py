class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''modification from problem "Course Schedule"
        '''
        # preMap = {i : [] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)
        # visitSet = set()
        # res = []
        # def dfs(crs):
        #     if crs in visitSet:
        #         return False
        #     if preMap[crs] == []:
        #         if crs not in res:
        #             res.append(crs)
        #         return True
        #     visitSet.add(crs)
        #     for pre in preMap[crs]:
        #         if not dfs(pre):
        #             return False
        #     visitSet.remove(crs)
        #     preMap[crs] = []
        #     if crs not in res:
        #             res.append(crs)
        #     return True

        # for crs in range(numCourses):
        #     if not dfs(crs): return []
        # return res
        '''neet
        '''
        # build adjacency list of prereqs
        prereq = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        # a course has 3 possible states:
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle 
        # unvisited -> crs not added to output or cycle
        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True # NOTE: important to return True!!!!
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output














