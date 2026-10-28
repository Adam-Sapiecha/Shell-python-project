import sys


def main():
    sys.stdout.write("$ ")
    tekst = input()
    if tekst == "echo" or tekst == "cd":
        pass
        main()
    else:
        print("Unknown command")
        main()
    pass




if __name__ == "__main__":
    main()
