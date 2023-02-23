class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hm = {}
        for i in range(len(heights)) :
            hm[heights[i]] = names[i]
        heights.sort(reverse = True)
        return [hm[i] for i in heights]