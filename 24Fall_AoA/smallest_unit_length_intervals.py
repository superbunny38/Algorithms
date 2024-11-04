def smallest_unit_length_intervals(points):
    points.sort()
    intervals = []
    for point in points:
        if not intervals:
            intervals = [[point,point+1]]
            continue
        elif point > intervals[-1][1]:
            intervals.append([point,point+1])
    return intervals

points = [-1,2,-3,0,5,-7]
print(smallest_unit_length_intervals(points=points))
