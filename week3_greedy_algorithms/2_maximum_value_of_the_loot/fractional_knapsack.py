# Uses python3
import sys

capacity = 50
values = [60 ,100, 120]
weights = [20, 50, 30]
def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    v_unit = []
    for w, v in zip(weights, values):
        v_unit.append((v/w, w))

    v_unit = sorted(v_unit, reverse=True)
    print(v_unit)
    i = 0
    while capacity > 0:

        carry = min(capacity, v_unit[i][1])
        value += carry*v_unit[i][0]
        capacity -= carry
        i += 1

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
