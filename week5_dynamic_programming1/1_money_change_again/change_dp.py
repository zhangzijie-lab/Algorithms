# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1, 3, 4]
    min_coins = [0]*(m+1)

    for i in range(1, m+1):
        nums = [min_coins[i-c] + 1 for c in coins if i>=c]
        min_coins[i] = min(nums)

    return min_coins[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
