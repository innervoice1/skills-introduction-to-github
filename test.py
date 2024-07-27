import math

"""
This is a Python script that demonstrates how to calculate the area of a rectangle and the square root of a number.
"""


# Function to calculate the area of a rectangle
def calculate_area(length, width):
    """
    Calculates the area of a rectangle.

    Parameters:
    - length (float): The length of the rectangle.
    - width (float): The width of the rectangle.

    Returns:
    - area (float): The area of the rectangle.
    """
    area = length * width
    return area

# Function to calculate the square root of a number
def calculate_square_root(number):
    """
    Calculates the square root of a number.

    Parameters:
    - number (float): The number to calculate the square root of.

    Returns:
    - square_root (float): The square root of the number.
    """
    square_root = math.sqrt(number)
    return square_root

# Prompt the user to enter the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate and print the area of the rectangle
area = calculate_area(length, width)
print("The area of the rectangle is:", area)

# Prompt the user to enter a number to calculate its square root
number = float(input("Enter a number to calculate its square root: "))

# Calculate and print the square root of the number
square_root = calculate_square_root(number)
print("The square root of", number, "is:", square_root)



# Create a new function to calculate the perimeter of a rectangle
def calculate_perimeter(length, width):
    """
    Calculates the perimeter of a rectangle.

    Parameters:
    - length (float): The length of the rectangle.
    - width (float): The width of the rectangle.

    Returns:
    - perimeter (float): The perimeter of the rectangle.
    """
    perimeter = 2 * (length + width)
    return perimeter

# Prompt the user to enter the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
# Calculate and print the perimeter of the rectangle
perimeter = calculate_perimeter(length, width)
print("The perimeter of the rectangle is:", perimeter)



# is there a way to run a small piece of code directly in vscode without running the whole file?
# Yes, you can run a small piece of code directly in VSCode using the Python Interactive window. To do this, follow these steps:
# 1. Open the Python file in VSCode.
# 2. Select the code snippet that you want to run.
# 3. Right-click on the selected code snippet.
# 4. Choose "Run Selection/Line in Python Interactive Window" from the context menu.

