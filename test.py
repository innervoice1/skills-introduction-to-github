import math

"""
This is a Python script that demonstrates how to calculate the area of a rectangle and the square root of a number.
"""


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
#Q: how to delete a branch in git in terminal?
# A: To delete a branch in Git using the terminal, you can use the following command:


# Create a function that inputs a string not more than 10 characters in length, does not allow vowels in it, else returns 
# an error message that the string is invalid as it contains vowels. If valid, print the string backwards and in uppercase.
import sys

def process_string():
    """
    Inputs a string not more than 10 characters in length, does not allow vowels in it, else returns an error message that the string is invalid as it contains vowels.
    If valid, prints the string backwards and in uppercase.
    """
    # Check if the command-line argument is provided
    if len(sys.argv) != 2:
        print("Error: Please provide a single string as a command-line argument.")
        return
    
    # Get the string from the command-line argument
    string = sys.argv[1]
    
    # Check if the string is valid
    if len(string) > 10:
        print("Error: The string is invalid as it contains more than 10 characters.")
    elif any(char in 'aeiouAEIOU' for char in string):
        print("Error: The string is invalid as it contains vowels.")
    else:
        # Print the string backwards and in uppercase
        reversed_string = string[::-1]
        uppercase_string = reversed_string.upper()
        print("The processed string is:", uppercase_string)

if __name__ == "__main__":
    process_string()

# test the above function
# python test.py "hello"
# python test.py "world"
# python test.py "python"
# python test.py "HELLO"
# python test.py "WORLD"
# python test.py "PYTHON"
# python test.py "helloworld"
# python test.py "HELLOWORLD"
# python test.py "PYTHONHELLO"
# also give a brief explanation for reason of that test case
# The test cases are as follows:
# 1. python test.py "hello": The string "hello" contains vowels, so it should return an error message.
# 2. python test.py "world": The string "world" does not contain vowels and is less than 10 characters, so it should print the reversed string in uppercase.
# 3. python test.py "python": The string "python" contains vowels, so it should return an error message.
# 4. python test.py "HELLO": The string "HELLO" contains vowels, so it should return an error message.
# 5. python test.py "WORLD": The string "WORLD" does not contain vowels and is less than 10 characters, so it should print the reversed string in uppercase.
# 6. python test.py "PYTHON": The string "PYTHON" contains vowels, so it should return an error message.
# 7. python test.py "helloworld": The string "helloworld" contains vowels, so it should return an error message.
# 8. python test.py "HELLOWORLD": The string "HELLOWORLD" contains vowels, so it should return an error message.
# 9. python test.py "PYTHONHELLO": The string "PYTHONHELLO" contains vowels, so it should return an error message.
# The test cases cover scenarios where the input string contains vowels, is longer than 10 characters, or is a valid string that can be processed.



