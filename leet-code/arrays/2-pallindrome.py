class solution :

    def is_palindrome(self, x) -> bool :
        temp = x 
        reverse = 0
        while x > 0 :
            reverse = ((reverse * 10) + (x % 10))
            x = x // 10
        return temp == reverse 

if __name__ == "__main__" :
    number = int(input(">"))
    result = solution()
    print(f"result : ",result.is_palindrome(number))
