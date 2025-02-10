
import data

# Write your functions for each part in the space below.

# Part 1
def first_element(nums:list[list[int]]) -> list[int]:
    first_list = []
    second_list = []
    for i in nums:
        if i:
            first_list.append(i)
    for i in first_list:
        second_list.append(i[0])
    return second_list


# Part 2
def x_coordinates(nums:list[data.Point]):
    new_list = []
    for i in nums:
        new_list.append(i.x)

    return new_list


# Part 3
def are_in_positive_quadrant(nums:list[data.Point]):
    new_list = []
    for Point in nums:
        if Point.x > 0 and Point.y > 0:
            new_list.append(Point)
    return new_list

# Part 4
def distance(n:data.Point, m:data.Point):
     return data.math.sqrt((n.x-m.x)**2 + (n.y-m.y)**2)


# Part 5
def manhattan_distance(n:data.Point, m:data.Point):
    q = (n.x-m.x)/2 + m.x
    d = (n.y-m.y)/2 + m.y
    return data.Point(q, d)

# Part 6
def distance_all(nums: list[data.Point]):
    new_list = []
    for i in nums:
        new_list.append(distance(i, data.Point(0,0)))
    return new_list


