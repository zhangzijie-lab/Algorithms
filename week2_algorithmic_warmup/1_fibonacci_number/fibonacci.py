# Uses python3
# O(n^2)
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())

# O(n)
def calc_fib_fast(n):
    f = [0]*(n+1)
    f[1] = 1
    if n <= 1:
        return f[n]

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]

print(calc_fib_fast(n))
print(calc_fib(n))
