#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        min_ = arr[0]
        max_ = arr[n-1]
        dif = max_ - min_
        for i in range(n) :
            if arr[i] - k < 0 :
                continue
            min_ = min(arr[0]+k,arr[i] - k) 
            max_ = max(arr[n-1] -k, arr[i-1] + k)
            dif = min(dif,max_- min_)
        return dif

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1
