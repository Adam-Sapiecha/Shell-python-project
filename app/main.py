import sys


def main():
    sys.stdout.write("$ ")
    tekst = input()
    if tekst == "echo":
        print(tekst)
        main()
    elif tekst == '':
        main()
    elif tekst == "exit":
        sys.exit()
    else:
        print(tekst + ": command not found")
        main()
    pass




if __name__ == "__main__":
    main()
