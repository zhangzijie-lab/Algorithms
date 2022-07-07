# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):

    #write your code here
    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)

    ps = sorted(segments, key=lambda x: x.end)

    points = [ps[0].end]
    cur = ps[0].end
    for i in range(1, len(ps)):
        if ps[i].start <= cur:
            continue
        else:
            cur = ps[i].end
            points.append(cur)

    
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
