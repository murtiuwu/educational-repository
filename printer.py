def printer(fill_inc=0):
    def fill(filling):
        global inc
        inc = fill_inc + filling

    def write(text):
        print(text)
        inc -= len(text)







