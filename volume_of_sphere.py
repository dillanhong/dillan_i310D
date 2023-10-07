import math

def calculate_volume_of_sphere(radius):
    """Calculate and print the volume of a sphere with the given radius."""
    pi = math.pi  # The mathematical constant pi

    # Calculate the volume using the formula
    volume = (4/3) * pi * (radius ** 3)

    # Print the result
    print(f"The volume of a sphere with radius {radius} is {volume:.2f} cubic units.")

# Calculate and print the volume for a sphere with radius 30
sphere_volume(30)

# Calculate and print the volume for a sphere with radius 40
sphere_volume(40)
