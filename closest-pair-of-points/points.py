from typing import List, Tuple
import math

Point = Tuple[float, float]

def distance(p1: Point, p2: Point) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair_of_points(points: List[Point]) -> Tuple[float, Point, Point]:
    points.sort()

    def closest_pair_recurse(sorting_points: List[Point]):
        q = len(sorting_points)
        if q <= 3:
            min_dist = float('inf')
            result = None
            for i in range(q):
                for j in range(i + 1, q):
                    d = distance(sorting_points[i], sorting_points[j])
                    if d < min_dist:
                        min_dist = d
                        result = (sorting_points[i], sorting_points[j])
            return min_dist, result[0], result[1]

        mid = q // 2
        left_half = sorting_points[:mid]
        right_half = sorting_points[mid:]

        left_min_dist, left_p1, left_p2 = closest_pair_recurse(left_half)
        right_min_dist, right_p1, right_p2 = closest_pair_recurse(right_half)

        glob_min_dist = min(left_min_dist, right_min_dist)
        glob_p1 = left_p1 if left_min_dist == glob_min_dist else right_p1
        glob_p2 = left_p2 if left_min_dist == glob_min_dist else right_p2

        strip = []
        mid_x = sorting_points[mid][0]
        for point in sorting_points:
            if abs(point[0] - mid_x) < glob_min_dist:
                strip.append(point)

        strip.sort(key=lambda p: p[1])

        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if strip[j][1] - strip[i][1] > glob_min_dist:
                    break
                d = distance(strip[i], strip[j])
                if d < glob_min_dist:
                    glob_min_dist = d
                    glob_p1 = strip[i]
                    glob_p2 = strip[j]

        return glob_min_dist, glob_p1, glob_p2

    return closest_pair_recurse(points)
