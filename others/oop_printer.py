
class Printer:

    def __init__(self, file, ink=0, splitter="\n\n----------\n\n"):
        self.ink = ink
        self.file = file
        self.splitter = splitter

    def check_ink(self):
        return f'\nyou have {self.ink} ink'

    def fill(self, filling):
        self.ink += filling
        return f'now, you have {self.ink} ink'

    def write(self, text_file):
        try:
            if text_file == self.file:
                raise
            with open(text_file, 'r') as read_file:
                text = read_file.read()

            if self.ink == 0:
                return "printer can't work"

            with open(self.file, 'a') as write_file:
                for letter in text:
                    if self.ink == 0:
                        write_file.write('...')
                        write_file.write(self.splitter)
                        return '\nhave no ink'
                    write_file.write(letter)
                    if letter in ['\n', ' ', '\t']:
                        self.ink += 1
                    self.ink -= 1
                write_file.write(self.splitter)
                return self.ink
        except ActiveException:

        except Exception as e:
            return f"file {text_file}{e} doesn't exist"

    def read(self):
        with open(self.file, 'r') as print_file:
            return print_file.read()


my_printer = Printer('filik', 19)
print(my_printer.write('qwert'))
print(my_printer.read())


# active exception [Errno 2] No such file or directory: 'qwert'

