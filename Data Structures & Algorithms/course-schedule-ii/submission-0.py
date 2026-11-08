class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visitSet = set()
        res = []
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            if crs not in res:
                    res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []
        return res