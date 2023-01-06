class solution :
    def reverse(self,arr) :
        return(arr[::-1])

# array reversal
if __name__ == "__main__" :
    a = input("enter a string : ")
    result = solution()
    print("reversed string : ",result.reverse(a))



