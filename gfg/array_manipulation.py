# link to problem  : https://www.hackerrank.com/challenges/crush/problem

# SOLUTION


class solution:
    def array_manipulation(self, n, queries):
        arr = [0] * n
        for i in queries:
            arr[i[0] - 1] += i[2]
            if i[1] != n:
                arr[i[1]] -= i[2]

        large = 0
        curr = 0
        for i in range(n):
            curr += arr[i]
            if curr > large:
                large = curr

        return large


if __name__ == "__main__":
    n, q = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(q)]

    result = solution()

    print("largest number : ", result.array_manipulation(n=n, queries=queries))
