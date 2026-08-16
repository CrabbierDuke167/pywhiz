import math


# Perimeter and Circumference

def perim_square(side):
    """Calculates the perimeter of a square"""
    if side < 0: return 0
    return 4 * side

def perim_rect(length, width):
    """Calculates the perimeter of a rectangle"""
    if length < 0 or width < 0: return 0
    return 2 * (length + width)

def perim_tri(a, b, c):
    """Calculates the perimeter of a triangle"""
    if a < 0 or b < 0 or c < 0: return 0
    return a + b + c

def circum_circle(radius):
    """Calculates the circumference of a circle"""
    if radius < 0: return 0
    return round(2 * math.pi * radius, 4)

def perim_polygon(sides, side_length):
    """Calculates the perimeter of a regular polygon"""
    if sides < 3 or side_length < 0: return 0
    return sides * side_length


# Area (2D Shapes)

def area_square(side):
    """Calculates the area of a square"""
    if side < 0: return 0
    return side * side

def area_rect(length, width):
    """Calculates the area of a rectangle"""
    if length < 0 or width < 0: return 0
    return length * width

def area_tri_base(base, height):
    """Calculates the area of a triangle given base and height"""
    if base < 0 or height < 0: return 0
    return 0.5 * base * height

def area_tri_herons(a, b, c):
    """Calculates the area of a triangle using Heron's formula"""
    s = (a + b + c) / 2
    val = s * (s - a) * (s - b) * (s - c)
    if val <= 0: return 0
    return round(math.sqrt(val), 4)

def area_circle(radius):
    """Calculates the area of a circle"""
    if radius < 0: return 0
    return round(math.pi * radius * radius, 4)

def area_rhombus(d1, d2):
    """Calculates the area of a rhombus given two diagonals"""
    if d1 < 0 or d2 < 0: return 0
    return (d1 * d2) / 2

def area_trapezium(a, b, height):
    """Calculates the area of a trapezium given parallel sides and height"""
    if a < 0 or b < 0 or height < 0: return 0
    return 0.5 * (a + b) * height


# Surface Area (3D Shapes)

def sa_cube(side):
    """Calculates the total surface area of a cube"""
    if side < 0: return 0
    return 6 * (side * side)

def sa_cuboid(l, b, h):
    """Calculates the total surface area of a cuboid"""
    if l < 0 or b < 0 or h < 0: return 0
    return 2 * ((l * b) + (b * h) + (h * l))

def sa_cylinder(r, h):
    """Calculates the total surface area of a solid cylinder"""
    if r < 0 or h < 0: return 0
    return round(2 * math.pi * r * (r + h), 4)

def sa_cone(r, l):
    """Calculates the total surface area of a solid cone given radius and slant height"""
    if r < 0 or l < 0: return 0
    return round(math.pi * r * (r + l), 4)

def sa_sphere(r):
    """Calculates the surface area of a sphere"""
    if r < 0: return 0
    return round(4 * math.pi * r * r, 4)

def sa_hemisphere(r):
    """Calculates the total surface area of a solid hemisphere"""
    if r < 0: return 0
    return round(3 * math.pi * r * r, 4)


# Volume (3D Shapes)

def vol_cube(side):
    """Calculates the volume of a cube"""
    if side < 0: return 0
    return side * side * side

def vol_cuboid(l, b, h):
    """Calculates the volume of a cuboid"""
    if l < 0 or b < 0 or h < 0: return 0
    return l * b * h

def vol_cylinder(r, h):
    """Calculates the volume of a cylinder"""
    if r < 0 or h < 0: return 0
    return round(math.pi * r * r * h, 4)

def vol_cone(r, h):
    """Calculates the volume of a cone given radius and vertical height"""
    if r < 0 or h < 0: return 0
    return round((1/3) * math.pi * r * r * h, 4)

def vol_sphere(r):
    """Calculates the volume of a sphere"""
    if r < 0: return 0
    return round((4/3) * math.pi * (r * r * r), 4)

def vol_hemisphere(r):
    """Calculates the volume of a hemisphere"""
    if r < 0: return 0
    return round((2/3) * math.pi * (r * r * r), 4)