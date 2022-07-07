# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = sorted([1, 5, 10], reverse=True)
    ans = 0

    for c in coins:
        ans += m // c
        m = m%c

    return ans


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
