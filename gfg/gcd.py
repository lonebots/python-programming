class solution:
    def gcd_recursion(self, a, b):
        def gcd(a, b):
            if b == 0:
                return a

            else:
                return gcd(b, a % b)

        return gcd(a, b)

    def gcd_eclidian(self, a, b):
        def gcd(a, b):
            if a == 0:
                return b
            if b == 0:
                return a

            # best case
            if a == b:
                return a

            if a > b:
                return gcd(a - b, b)
            return gcd(a, b - a)

        return gcd(a, b)


def main(args=None):
    result = solution()

    a, b = map(int, input("enter a and b -> ").split())

    # gcd with recursion
    print("gcd recursion : ", result.gcd_recursion(a, b))

    # gcd with eclidian method, still uses recursion
    print("gcd recursion(euclidian) : ", result.gcd_eclidian(a, b))


if __name__ == "__main__":
    main()
