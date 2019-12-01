print("Create a file and copy the content into that file from abc.txt...........")
import os
from sys import *


def Create_copy(path):
    #print("The path is::", path)

    cobj=open(argv[1],'r')
    copy_content=cobj.read()
    #print("Copy Content",copy_content)
    fobj = open(argv[2], 'w')
    fobj.write(copy_content)



def main():
    print("File name", argv[1])
    if (len(argv) < 1) or (len(argv) > 3):
        print("Error : Invalid number of argumnets")
    try:
        Create_copy(argv[1])
    except Exception as E:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
