# Jason Zhang
# jasozhang
# 112710259
# CSE 101
# Lab Assignment 9

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Line:
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def check_point(self, p):
        return p.y - self.m * p.x - self.b == 0


def find_points_on_line(coordinates, m, b):
    poin = []
    for i in coordinates:
        if Line(m, b).check_point(Point(*i)):
            poin.append(Point(*i))
    return poin


