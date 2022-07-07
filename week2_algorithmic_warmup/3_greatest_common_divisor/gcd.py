# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_fast(a, b):

    aprime = a%b

    if min(aprime, b) == 0:
        return max(aprime, b)
    else:
        return gcd_fast(b, aprime)

a, b = 100, 35
gcd_fast(b, a)
gcd_naive(a, b)
if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
