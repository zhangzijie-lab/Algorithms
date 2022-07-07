# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    numfills = 0
    curfill = 0

    stops = [0] + stops + [distance]

    n = len(stops) - 2
    while curfill < n:
        lastfill = curfill

        while (curfill <= n) & (stops[curfill+1] - stops[lastfill] < tank):
            curfill += 1
        
        if curfill  == lastfill:
            return 'Impossible'

        if curfill <= n:
            numfills += 1
    

    return numfills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
