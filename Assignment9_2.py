print("Current directory File Exist or not and read file...........")
import os
from sys import *


def Check_File(path):
    print("The path is::", path)
    flags = os.path.isfile(path)
    #print("Flag:::",flags)

    if flags:
        print("File is exists with path:::", os.path.abspath(path))
        fobj=open(path,'r')
        print(fobj.read())
    else:
        print("Invalid File Name")


def main():
    print("File name", argv[1])
    if (len(argv) < 1) or (len(argv) > 2):
        print("Error : Invalid number of argumnets")
    try:
        Check_File(argv[1])
    except Exception as E:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
