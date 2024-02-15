def printer(fill_ink=0):

    ink = fill_ink

    def check_ink():
        nonlocal ink
        print(f'\nyou have {ink} ink')

    def fill(filling):
        nonlocal ink
        ink += filling
        return ink

    def write(text):
        nonlocal ink
        for letter in text:
            if ink == 0:
                print('\nhave no ink')
                break
            print(letter, end='')
            ink -= 1
        return ink

    printer.fill = fill
    printer.write = write
    printer.check_inc = check_ink
    return printer

my_printer = printer(13)

my_printer.write('hello')
my_printer.write('\nhello world')
my_printer.fill(24)
my_printer.write('\nhello world')
my_printer.check_inc()

