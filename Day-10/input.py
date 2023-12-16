import os 


"""
folders = input("Please provide a list of folder names with spaces in between the names: ").split()
"""
'''
for folder in folders:
    files = os.listdir(folder)
    print(" ==== listing files for the folder-" + folder)
    # By default, the listdir() method returns a list of filenames in the specified directory.
    # The list is sorted in alphabetical order.
    # You can specify the sorting order by passing the optional keyword argument 'sort' to the listdir() method.
    # By default each iteration is displayed on a separate line.
    for file in files:
        print(file)
'''

"""
# For exception handling, you can use try-except blocks.
# The try block contains the code that might raise an exception.
# The except block contains the code that handles the exception.

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("The folder " + folder + " does not exist. Please provide a valid  folder name: ")
        break 
    except PermissionError:
        print("The folder " + folder + " does not have permission to read. Please provide a valid  folder name: ")
        break
    print(" ==== listing files for the folder-" + folder)

    for file in files:
        print(file)
"""   


'''
folders = input(
    "Enter folder names separated by commas (,): "
).split(",")

for folder in folders:
    encountered_error = False  # New flag to track error state
    try:
        files = os.listdir(folder)
    except Exception as e:
        print(f"Error accessing folder '{folder}': {e}.")
        encountered_error = True
        # Only ask for new folder if error occurred
        while encountered_error:
            new_folder = input(
                "Please enter a valid folder name: "
            ).strip()
            try:
                files = os.listdir(new_folder)
                encountered_error = False  # Reset flag after valid folder
                break
            except Exception as e:
                print(
                    f"Error accessing folder '{new_folder}': {e}. "
                    "Please try again."
                )

    if not encountered_error:  # Check if error occurred for current folder
        print(f"\n==== Listing files for folder '{folder}':")
        for file in files:
            print(file)

print("\nFinished listing files.")
'''

def list_files(folder_name):
    try:
        files = os.listdir(folder_name)
        print(f"\n==== Listing files for folder '{folder_name}':")
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error accessing folder '{folder_name}': {e}.")

# Get folder names from user
folders = input(
    "Enter folder names separated by commas (,): "
).split(",")

# Process each folder individually
for folder in folders:
    list_files(folder.strip())  # Strip whitespace to avoid errors

print("\nFinished listing files.")

