print("Check content of 2 file as Demo.txt and Hello.txt...........")
from sys import *


def Search_content(path,search):
    # print("The path is::", path)
    copy_content = list()
    cobj = open(argv[1],'r')
    #copy_content = cobj.readlines().find("Hello")
    #print(copy_content)
    flags=False
    icnt=0
    #cobj.readlines()
    for rli in cobj:
        print(rli)

        words = rli.split()
        print (len(words), words)
        for str_w in words:

            if search in str_w:
                #flags=True
                icnt=icnt+1
                #print("Tr")
            else:
                #flags=False
                print("F")

    if icnt ==0:
        print("No String found")
    else:
        print("The Count of String is:::",icnt)


def main():
    print("File name", argv[1])
    if (len(argv) < 1) or (len(argv) > 3):
        print("Error : Invalid number of argumnets")
    try:
        Search_content(argv[1],argv[2])
    except Exception as E:
        print("Error : Invalid input")


if __name__ == "__main__":
    main()
