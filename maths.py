import math

# Volume Functions
def volume_cube_cuboid(l, w, h): return l * w * h
def volume_pyramid(l, w, h): return (l * w * h) / 3
def volume_cylinder(r, h): return math.pi * r**2 * h
def volume_sphere(r): return (4 / 3) * math.pi * r**3
def volume_cone(r, h): return (1 / 3) * math.pi * r**2 * h
def volume_ellipsoid(a, b, c): return (4 / 3) * math.pi * a * b * c
def volume_torus(R, r): return (math.pi * r**2) * (2 * math.pi * R)
def volume_hexagonal_prism(a, h): return ((3 * math.sqrt(3)) / 2) * a**2 * h

# Surface Area Functions
def surface_cube_cuboid(l, w, h): return 2 * (l*w + w*h + h*l)
def surface_pyramid(l, w, h): return (l * w) + (l * math.sqrt((w/2)**2 + h**2)) + (w * math.sqrt((l/2)**2 + h**2))
def surface_cylinder(r, h): return 2 * math.pi * r * (r + h)
def surface_sphere(r): return 4 * math.pi * r**2
def surface_cone(r, h): return math.pi * r * (r + math.sqrt(h**2 + r**2))
def surface_ellipsoid(a, b, c): return 4 * math.pi * (((a**p * b**p + a**p * c**p + b**p * c**p)/3)**(1/p)) if (p := 1.6) else 0
def surface_torus(R, r): return 4 * math.pi**2 * R * r
def surface_hexagonal_prism(a, h): return 6 * a * h + 3 * math.sqrt(3) * a**2

# Unit Conversion
def convert_to_meters(val, unit):
    return {
        'mm': val / 1000,
        'cm': val / 100,
        'm': val
    }.get(unit, val)

# Input helpers
def get_float(prompt): 
    while True:
        try: return float(input(prompt))
        except ValueError: print("Invalid number. Try again.")

def get_unit():
    while True:
        unit = input("Select unit (mm/cm/m): ").lower()
        if unit in ['mm', 'cm', 'm']: return unit
        print("Invalid unit. Use mm, cm or m.")

def label(unit): return f"{unit}³", f"{unit}²"

# Banner
print("----------------")
print("Volume and Surface area Calculator")
print("Created by: https://github.com/Kaustav-codes")
print("----------------")

# Main loop
while True:
    print("\nChoose shape:")
    print("1. Cube/Cuboid")
    print("2. Pyramid (Right Rectangular)")
    print("3. Cylinder")
    print("4. Sphere")
    print("5. Cone")
    print("6. Ellipsoid")
    print("7. Torus (Donut)")
    print("8. Hexagonal Prism")
    print("0. Exit")
    
    choice = input("Enter choice (0-8): ")
    if choice == "0":
        print("Thank you for using the Geometry Calculator!")
        break

    unit = get_unit()

    if choice == "1":
        l = convert_to_meters(get_float("Length: "), unit)
        w = convert_to_meters(get_float("Width: "), unit)
        h = convert_to_meters(get_float("Height: "), unit)
        v, a = volume_cube_cuboid(l, w, h), surface_cube_cuboid(l, w, h)

    elif choice == "2":
        l = convert_to_meters(get_float("Length: "), unit)
        w = convert_to_meters(get_float("Width: "), unit)
        h = convert_to_meters(get_float("Height: "), unit)
        v, a = volume_pyramid(l, w, h), surface_pyramid(l, w, h)

    elif choice == "3":
        r = convert_to_meters(get_float("Radius: "), unit)
        h = convert_to_meters(get_float("Height: "), unit)
        v, a = volume_cylinder(r, h), surface_cylinder(r, h)

    elif choice == "4":
        r = convert_to_meters(get_float("Radius: "), unit)
        v, a = volume_sphere(r), surface_sphere(r)

    elif choice == "5":
        r = convert_to_meters(get_float("Radius: "), unit)
        h = convert_to_meters(get_float("Height: "), unit)
        v, a = volume_cone(r, h), surface_cone(r, h)

    elif choice == "6":
        a1 = convert_to_meters(get_float("a-axis: "), unit)
        b = convert_to_meters(get_float("b-axis: "), unit)
        c = convert_to_meters(get_float("c-axis: "), unit)
        v, a = volume_ellipsoid(a1, b, c), surface_ellipsoid(a1, b, c)

    elif choice == "7":
        R = convert_to_meters(get_float("Major Radius (R): "), unit)
        r = convert_to_meters(get_float("Minor Radius (r): "), unit)
        if R <= r:
            print("Error: Major radius must be greater than minor radius.")
            continue
        v, a = volume_torus(R, r), surface_torus(R, r)

    elif choice == "8":
        a1 = convert_to_meters(get_float("Base edge: "), unit)
        h = convert_to_meters(get_float("Height: "), unit)
        v, a = volume_hexagonal_prism(a1, h), surface_hexagonal_prism(a1, h)

    else:
        print("Invalid input.")
        continue

    v_unit, a_unit = label(unit)
    print(f"Volume: {round(v, 4)} {v_unit}")
    print(f"Surface Area: {round(a, 4)} {a_unit}")
