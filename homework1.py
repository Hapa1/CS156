# -----------------------------------------------------------------------------
# Name:        homework1
# Purpose:     Practice writing Python functions
#
# Author: Ryan Moore
# -----------------------------------------------------------------------------
"""
Implement some helper functions that will be useful in subsequent assignments
"""


def manhattan_distance(point1, point2):
    """
    Compute the Manhattan distance between two points.
    :param point1 (tuple) representing the coordinates of a point in a plane
    :param point2 (tuple) representing the coordinates of a point in a plane
    :return: (integer)  The Manhattan distance between the two points
    """
    (x1, y1) = point1
    (x2, y2) = point2
    return (abs(x1 - x2) + abs(y1 - y2))


def min_distance(point1, other_points): #TODO: ADD IF NONE
    """
    Find the minimum Manhattan distance from point1 to the other points
    :param point1 (tuple) representing the coordinates of a point in a plane
    :param other_points (set of tuples) representing several points in a plane
    :return: (integer) maximum Manhattan distance from point1 to the other
    points

    """
    list = [manhattan_distance(point1,point) for point in other_points]
    return min(list)


def farthest_point(point1, other_points): #TODO: REFACTOR
    """
    Find the coordinates of the farthest point to point1
    :param point1 (tuple) representing the coordinates of a point in a plane
    :param other_points(set of tuples) representing several points in a
    plane
    :return: (tuple) the coordinates of the farthest point to point1

    """
    list = []
    for point in other_points:
        list.append(manhattan_distance(point1, point))
    return other_points[list.index(max(list))]



def farthest_distance(points):
    """
    Find the maximum Manhattan distance between all the points given
    :param points(list of tuples) representing several points in a
    plane
    :return: (integer) maximum Manhattan distance between any two points
    in the list given.
    """
