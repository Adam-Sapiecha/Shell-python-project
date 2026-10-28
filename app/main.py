import sys


def main():
    sys.stdout.write("$ ")
    tekst = input()
    if tekst == "echo" or tekst == "cd":
        pass
        main()
    elif tekst == '':
        main()
    else:
        print(tekst + ": command not found")
        main()
    pass




if __name__ == "__main__":
    main()
