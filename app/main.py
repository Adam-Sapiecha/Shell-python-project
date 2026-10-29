import sys

class Command:
    @staticmethod
    def run():
        print('$ ')
class EchoCommand(Command):
    @staticmethod
    def run(args):
        print(" ".join(args[1:]))
class ExitCommand(Command):
    @staticmethod
    def run(args):
        sys.exit()
class InvalidCommand(Command):
    @staticmethod
    def run(args):
        print('Unknown command')
class LsCommand(Command):
    @staticmethod
    def run(args):
        print('not implemented yet')



def main():
    while True:
        tekst = input('$ ')
        args = list(tekst.split())
        dic = {
            'echo' : EchoCommand.run,
            'ls' : LsCommand.run,
            'exit' : ExitCommand.run
        }
        if not args:
            continue
        command = dic.get(args[0], InvalidCommand.run)
        command(args)


if __name__ == "__main__":
    main()
