import geometry_utils

operations = {
    "circle_area": geometry_utils.circle_area,
    "circle_perimeter": geometry_utils.circle_perimeter,
    "rectangle_area": geometry_utils.rectangle_area,
    "rectangle_perimeter": geometry_utils.rectangle_perimeter,
    "triangle_area": geometry_utils.triangle_area
}

print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter")

op = input("Enter the operation you want to perform: ")

try:
    if "circle" in op:
        r = float(input("Enter radius: "))
        result = operations[op](r)

    elif "rectangle" in op:
        w = float(input("Enter width: "))
        h = float(input("Enter height: "))
        result = operations[op](w, h)

    elif "triangle" in op:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        result = operations[op](b, h)

    print("Result:", result)

except KeyError:
    print("Invalid operation.")
except ValueError as e:
    print("Input Error:", e)

