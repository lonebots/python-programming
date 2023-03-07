class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # m_map = {}
        # for i in range(n) :
        #     m_map[manager[i]] = m_map.get(manager[i],[]) + [i]

        m_map = defaultdict(list)
        for i in range(len(manager)):
            m_map[manager[i]].append(i)

        print(m_map)

        def dfs (m) :
            report_time = 0 
            for employee in m_map[m] :
                report_time = max(dfs(employee) + informTime[m], report_time)

            return report_time

        return dfs(headID)
