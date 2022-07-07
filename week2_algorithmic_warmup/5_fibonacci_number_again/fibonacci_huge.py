# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

def fibonacci_fast(n, m):
    fib = [0, 1]

    if n <= 1:
        return n
    else:
        for i in range(2, n+1):
            cur = fib[i-1] + fib[i-2]
            fib.append(cur)
        
    return fib[n]

n = 10
m = 1


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
