"""
CP1404/CP5632 Practical
Cleanup file names
"""
import os


def main():
    """Program to clean file names."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk("."):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

    for filename in filenames:
        current_name = os.path.join(directory_name, filename)
        new_name = os.path.join(directory_name, get_fixed_filename(filename))
        os.rename(current_name, new_name)
        print(f"Successfully changed {current_name} to {new_name}")


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    current_name = filename.replace(".TXT", ".txt").replace(".txt", "")
    for index, character in enumerate(current_name):
        if character.isspace():
            character = "_"

        elif character.isalpha():
            try:
                previous_character = current_name[index-1]
                next_character = current_name[index+1]
                if next_character.isupper():
                    character += "_"
                elif previous_character == "_":
                    character = character.upper()
            except IndexError:
                pass

        new_name += character
    new_name += ".txt"
    # print(new_name)
    return new_name


main()
# get_fixed_filename('MyAngel Dior.txt') testing
