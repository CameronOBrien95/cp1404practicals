"""
CP1404/CP5632 Practical
"""
import shutil
import os


def main():
    """."""
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics/Christmas')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """."""
    name_to_change = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    caps_counter = 0
    if not "_" in name_to_change:
        for char in name_to_change:
            if char.isupper():
                if caps_counter == 0:
                    new_name += char
                elif caps_counter > 0:
                    new_name += "_" + char
            else:
                new_name += char
            caps_counter += 1
    else:
        new_name = name_to_change
    return new_name


def demo_walk():
    """."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            old_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(old_name, new_name)


main()
# demo_walk()