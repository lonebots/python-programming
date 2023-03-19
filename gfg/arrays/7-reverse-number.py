class solution():
    rev = 0
    def reverse (self,num) :
        # base condition
        if num != 0 :
            return num % 10

        # recursion
        return self.rev * 10 + self.reverse(num//10)

if __name__ == "__main__" : 
    num = int(input("enter number > "))

    result = solution()

    print("reverse", result.reverse(num))