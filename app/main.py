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
        print(' '.join(args) + ': command not found')
class LsCommand(Command):
    @staticmethod
    def run(args):
        print('not implemented yet')
class TypeCommand(Command):
    @staticmethod
    def run(args):
        if ' '.join(args[1:]) in Dic.dic:
            print(' '.join(args[1:]) + ' is a shell builtin')
        else: 
            print(' '.join(args[1:]) + ': not found')     
class Dic:
    dic = {
        'echo' : EchoCommand.run,
        'ls' : LsCommand.run,
        'exit' : ExitCommand.run,
        'type' : TypeCommand.run
    }


def main():
    while True:
        tekst = input('$ ')
        args = list(tekst.split())
        if not args:
            continue
        command = Dic.dic.get(args[0], InvalidCommand.run)
        command(args)


if __name__ == "__main__":
    main()
