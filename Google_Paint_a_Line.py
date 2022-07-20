

"""
Problem Statement:
There is a Line (Like X axis) which we need to paint. you are given a list of pairs which is needs to be painted, such as
(4, 10), (7, 13), (16,20), (1, 40). There is a cost to paint a particular area which is equal to the distance.
Such as for (4, 10) the cost is 10 - 4 = 6. and so on. you have write the code to calculate the cost required to paint
each of the given pairs. note that if the area is already painted once, no need to paint it again.

Example.
first we paint (4, 10), which costs 6, then we paint (7, 13), but we already know that 7-10 is already painted, so we
will paint only 10-13 which will cost us 3 only. Then we will paint (16, 20) which will cost 4, and finally the pair (1-40)
will be painted which will cost (40 - 1) - (10-4) - (13-10) - (20-16) which is 26. so the output array will be [6, 3, 4, 26]
"""



# previous_x2 = 0
# cost_of_paint = list()
#
# for i, axis_points in enumerate(line_X):
#     print(f"Value {i}: {axis_points}")
#     # if i == 0:
#     #     cost = axis_points[1]-axis_points[0]
#     #     previous_x2 = axis_points[-1]
#     # else:
#     #     if previous_x2 > axis_points[0]:
#     #         print("IF BLOCK")
#     #         already_painted = previous_x2 - axis_points[0]
#     #         cost = axis_points[1] - previous_x2
#     #     else:
#     #         print("ELSE BLOCK")
#     #
#     #         cost = axis_points[1] - axis_points[0]
#
#
#     cost_of_paint.append(cost)

def paintLine(points):
    mx = 0
    for x1, x2 in points:
        mx = max(mx, x2)
    mp = [False] * mx
    costs = []
    print(f" MAX: {mx}, MP: {len(mp)}")
    for x1, x2 in points:
        cost = 0
        print(f"AXIS: {x1,x2}")
        for i in range(x1, x2):
            if not mp[i]:
                mp[i] = True
                cost += 1
        costs.append(cost)
    return costs

print("COST OF PAINT: ", paintLine(points = [(4, 10), (7, 13), (16,20), (1, 40)]) )



