
def proper_fractions(n):
    def ntsqrt(n):
        sgn = 0
        if n < 0:
            sgn = -1
            n = -n
        val = n
        while True:
            last = val
            val = (val + n / val) * 0.5
            if abs(val - last) < 1e-9:
                break
        if sgn < 0:
            return complex(0, val)
        return val

    def is_prime(n):
        if n % 2 == 0 and n > 2:
            return False
        return all(n % i for i in range(3, int(ntsqrt(n)) + 1, 2))

    def gcd(x,y):
        while y:
            (x, y) = (y, x % y)
        return x

    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        count = 0
        if is_prime(n):
            return n - 1
        else:
            for num in range(1,n):
                denom = gcd(n,num)
                if denom == 1:
                    count += 1
            return count


if __name__ == "__main__":
    test = [1,2,5,15,25]
    for i in test:
        print(str(i) + ": " + str(proper_fractions(i)))
