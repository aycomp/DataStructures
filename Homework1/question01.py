# Question 1 (10%)

import math

# You are given a list of points of the form
# [(x1,y1), (x2,y2), ... ]
#
# You need to find the radius of the smallest circle
# centered at (0,0) that will cover all these points.
#
# The square root function is available as math.sqrt(x)
#
# Fill in the implementation of the function below accordingly:

def min_cover_radius(points):
    radius, tmp = 0, 0
    for i in points:
        tmp = math.sqrt(((i[0]-0) * (i[0]-0)) + ((i[1]-0) * (i[1]-0)))
        if(tmp > radius):
            radius = tmp
    return radius

# Examples:
list1 = [(1,4), (2,3), (3,3), (-1, 5), (6,7)]
list2 = [(245,400), (-123,233), (332.22,-32), (-12, 133), (336,37)]


print(min_cover_radius(list1))
print(min_cover_radius(list2))

# min_cover_radius(list1) should return 9.219544457292887
# min_cover_radius(list2) should return 469.0682253148256
