'''
time complexity : O(n^2) 
space complexity : O(1) - inplace
'''

class solution:
    def selection_sort(self,arr):
        n = len(arr)
        for i in range(n) :
            curr_min  = arr[i]
            min_pos = i
            for j in range(i+1,n) :
                if arr[j] < curr_min :
                    curr_min = arr[j]
                    min_pos = j
            arr[i],arr[min_pos] = arr[min_pos],arr[i] # reduce the number of total swappings
        return arr
            
  

T = int(input('test cases > '))

for cases in range(T):
    # input
    arr = list(map(int,input('enter array > ').split()))

    result = solution()

    print(result.selection_sort(arr))
