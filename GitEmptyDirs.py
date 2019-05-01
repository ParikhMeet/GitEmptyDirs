import os
from sys import argv
from shutil import copy2


def main():
    dirName = argv[1]
    listOfEmptyDirs = [dirpath for (dirpath, dirnames, filenames) in os.walk(
        dirName) if len(dirnames) == 0 and len(filenames) == 0]

    for elem in listOfEmptyDirs:
        print(elem)
        copy2(".gitignore", elem)


if __name__ == '__main__':
    main()
