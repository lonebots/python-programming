class solution : 
    def search (self,arr,key,l,r) :
        if (l>r) :
            return -1 
        else :
            m = l + (r-l)//2
            if (arr[m] == key) :
                return m 
            elif (key < arr[m]) :
                return self.search(arr,key,l,m-1) 
            else :
                return self.search(arr,key,m+1, r)
    # base condition

    # recursion

if __name__ == "__main__":
    arr = list(map(int,input('enter array > ').split()))
    key = int(input('search key : '))


    result = solution()
    print('result : ',result.search(arr,key,0,len(arr)-1))