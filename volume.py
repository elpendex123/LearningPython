import math

def calculate_sphere_properties(radius):
    # Calculate volume (V)
    volume = (4/3) * math.pi * radius**3

    # Calculate surface area (A)
    surface_area = 4 * math.pi * radius**2

    return volume, surface_area

# Input: Radius of the sphere
radius_input = float(input("Enter the radius of the sphere: "))

# Calculate properties
volume, surface_area = calculate_sphere_properties(radius_input)

# Output the results
print(f"Volume of the sphere: {volume:.2f} cubic units")
print(f"Surface area of the sphere: {surface_area:.2f} square units")
