class Solution:
    def nextGreaterElement(self, n: int) -> int:
        '''WRONG ANSWER'''
        # l = sorted(list(str(n)))[::-1]
        # newN = int(''.join(l))
        # if newN > (2 ** 31) -1 or newN <= n:
        #     return -1 
        # else:
        #     return newN
        

        digits = list(str(n))
        i = len(digits) - 1 

        while i - 1 > 0 and digits[i] <= digits[i-1] :
            i -= 1
        if i == 0 : return -1 # the number itself is the largest number posible with the given combination of digits

        j = i 
        while j + 1 < len(digits) and digits[j+1] > digits[i-1] :
            j+= 1 
        
        digits[i-1],digits[j] = digits[j],digits[i-1]
        digits[i:] = digits[i:][::-1]
 
        num = int(''.join(digits))

        return num if num <= (2**31)-1 and num > n else  -1
 