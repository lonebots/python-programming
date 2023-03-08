class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        self.answers = []

        for i in range(len(l)) :
            left = l[i]
            right = r[i] + 1

            # edge case 
            if right - left < 2 :
                self.answers.append('false')
            
            arr = sorted(nums[left:right])
            check = arr[1] - arr[0]

            print(arr)
            flag = True
            for j in range(1,len(arr)) :
                if arr[j] - arr[j-1] != check :
                    print('hi')
                    flag = False
                    break

            # out of loop
            self.answers.append(flag)

        return self.answers