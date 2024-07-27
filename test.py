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


# how to know which branch are you currently on in git?
# To know which branch you are currently on in Git, you can use the following command:
# Q:  where can we see the current branch in vscode?
# Q: how to stage changes in git using vscode because when i commit it says do you want to stage changes first?
# A: To stage changes in Git using VSCode, you can follow these steps:
# 1. Open the file that you want to stage changes for.
# 2. Make the necessary changes to the file.
# 3. Save the changes by pressing "Ctrl + S" or "Cmd + S" on Mac.
# 4. Open the Source Control view by clicking on the Source Control icon in the Activity Bar on the side of the window.
# 5. You will see a list of changed files in the Source Control view.
# 6. Click on the "+" icon next to the file you want to stage changes for. This will stage the changes.
# 7. Once you have staged all the changes you want to commit, enter a commit message in the text box at the top of the Source Control view.
# 8. Press "Ctrl + Enter" or click on the checkmark icon to commit the changes.
# 9. If you see a message asking you to stage changes first, follow the steps above to stage the changes before committing.

# q: if i have locally committed changes in a branch and want to merge it with the main branch, how can i do that?
# A: To merge locally committed changes from a branch into the main branch, you can follow these steps:\
# 1. Make sure you are on the branch that you want to merge changes from (e.g., feature-branch).
# 2. Commit your changes to the branch using the following commands:
# git add .
# git commit -m "Commit message"
# 3. Switch to the main branch using the following command:
# git checkout main
# 4. Merge the changes from the feature branch into the main branch using the following command:
# git merge feature-branch
# 5. Resolve any merge conflicts if necessary.
# 6. Push the changes to the remote repository using the following command:
# git push origin main
# This will merge the changes from the feature branch into the main branch and push the changes to the remote repository.
# Q: Why can't i first push the changes to the remote repository and then merge the branch with the main branch?
# A: You can push the changes to the remote repository before merging the branch with the main branch, but it is generally recommended to merge the changes locally first to resolve any conflicts and ensure that the changes are integrated correctly. Pushing the changes to the remote repository before merging can lead to conflicts with the main branch if other developers have made changes in the meantime. By merging locally first, you can resolve any conflicts and ensure that the changes are integrated smoothly before pushing them to the remote repository.
#Q: how to switch to main branch in git in terminal?
# A: To switch to the main branch in Git using the terminal, you can use the following command:
# git checkout main
#Q: and how to switch back to the feature branch?
# A: To switch back to the feature branch from the main branch, you can use the following command:
#Q: how to get a list of all branches in git?
# A: To get a list of all branches in Git, you can use the following command:



