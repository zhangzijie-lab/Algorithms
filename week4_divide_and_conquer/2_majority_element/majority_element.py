# Uses python3
import sys

def get_majority_element(a):
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]
    #write your code here
    count = {}
    n = len(a)
    for i in range(len(a)):
        count[a[i]] = count.get(a[i], 0) + 1
        if count.get(a[i], 0) > (n/2):
            return 1

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
