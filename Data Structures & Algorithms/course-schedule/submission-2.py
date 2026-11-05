class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        T: O(n + p)!!!!
        '''
        # map each course to prereq list
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False # crs is revisited => detected loop!!!
            if preMap[crs] == []:
                return True # crs has no prereq
            visitSet.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False # NOTE: nice trick, if found any, then return False immediately
            visitSet.remove(crs) # CRITICAL!!!! remove since we finished visiting it in this path!!!!!
            preMap[crs] = [] # CRITICAL!!! if crs is revisited, no need to repeat work!!!!
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
            
        


