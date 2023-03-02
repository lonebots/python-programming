# medium question
class Solution:
    def compress(self, chars: List[str]) -> int:
        # pointers
        idx = i = 0
        while i < len(chars) :
            j = i 
            while j < len(chars) and chars[j] == chars[i] :
                j += 1 

            chars[idx] = chars[i]
            idx += 1
            if j - i > 1 :
                count = str(j - i)
                for digit in count :
                    chars[idx] = digit
                    idx += 1
            i = j
        return idx