class Solution:
    def countAsterisks(self, s: str) -> int:
        count_star = 0
        bar = 0 
        for char in s : 
            if char == "|" :
                if bar < 2 :
                    bar += 1 
                else :
                    bar -= 1
            if char == "*" and bar != 1 :
                count_star += 1

        return count_star