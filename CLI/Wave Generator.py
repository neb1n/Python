import os


def generate_square_wave():
    input_string = input("What is your number")
    # making it a list
    amplen = [(int(input_string[v]), int(input_string[v+1])) for v in range(0, len(input_string), 2)]

    #what is the width
    total_width = sum(length for v, length in amplen)

    #making the grid and stuff
    grid = [['.' for v in range(total_width)] for v in range(10)]

    pos = 0

    for maximum, length in amplen:
        #making the wave
        for v in range(length):
            if maximum > 0:
                grid[9 - maximum][pos + v] = '@'
            #i don't get this
            if v == 0 and pos > 0:
                prev_amplitude = amplen[amplen.index((maximum, length)) - 1][0]
                for b in range(min(prev_amplitude, maximum), max(prev_amplitude, maximum) + 1):
                    grid[9 - b][pos] = '@'
        pos += length

    # print
    for row in grid:
        print(''.join(row))

    ret = input("Restart? y/n")
    if ret == "y":
        generate_square_wave()
        os.system('CLS')
    else:
        quit()

generate_square_wave()
