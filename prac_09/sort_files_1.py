import os
import shutil


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue

        extension = filename.split(".")[1]
        # print(extension)

        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        # print(f"{extension} / {filename}")
        shutil.move(filename, f"{extension}/" + filename)


main()

