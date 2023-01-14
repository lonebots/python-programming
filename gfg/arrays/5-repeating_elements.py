class solution:
    def findrepeatingelement(self, arr):
        # 1. naive approach
        # for i in range(len(arr)):
        #     for j in range(i + 1, len(arr)):
        #         if arr[i] == arr[j]:
        #             return arr[j]

        # return -1

        ele_count = {}
        for i in range(len(arr)):
            if arr[i] in ele_count.keys():
                ele_count[arr[i]] += 1
                return arr[i]
            else:
                ele_count[arr[i]] = 1

        return -1


if __name__ == "__main__":
    arr = list(map(int, input("array :").split()))

    result = solution()

    print(" first repeating element : ", result.findrepeatingelement(arr))
