def circle_area(radius):
    if radius <= 0:
        raise ValueError("Dimensions must be strictly positive.")
    return 3.14 * radius * radius

def circle_perimeter(radius):
    if radius <= 0:
        raise ValueError("Dimensions must be strictly positive.")
    return 2 * 3.14 * radius

def rectangle_area(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be strictly positive.")
    return width * height

def rectangle_perimeter(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Dimensions must be strictly positive.")
    return 2 * (width + height)

def triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Dimensions must be strictly positive.")
    return (base * height) / 2