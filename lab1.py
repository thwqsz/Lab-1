#
# import time
#
#
# def draw_line(offset=0, length=1, color=222):
#     line = ' ' * length
#     print(f'{" " * offset}\x1b[48;5;{color}m{line}\x1b[0m')
#
#
# def romb():
#     height = 15
#     center = height//2
#     offset = height//2
#     step = 1
#     length = 1
#     print(height, center, offset)
#     colors = [222, 157]
#     while True:
#         for color in colors:
#             for line in range(height):
#                 draw_line(offset, length, color)
#                 if line < center:
#                     offset -= step
#                     length += step*2
#                 else:
#                     offset += step
#                     length -= step*2
#             print(f'\x1b[{height+2}A')
#             print(f'\x1b[{offset}D')
#             length = 1
#             offset = height//2
#             time.sleep(2)
#
#
#
#
#
# if __name__ == '__main__':
#     romb()


# 1. ФЛАГ Бенина

print('#1')
red = '\x1b[48;5;196m'
yellow = '\x1b[48;5;220m'
green = '\x1b[48;5;82m'
stop = '\x1b[0m'
length = 20


def draw_line(color, ln):
    line = ' '*20
    print(color, line, stop, end='')


def flag_maker():
    for i in range(6):
        if i < 3:
            draw_line(green, length)
            draw_line(yellow, length)
            draw_line(yellow, length)
            print()
        else:
            draw_line(green, length)
            draw_line(red, length)
            draw_line(red, length)
            print()

flag_maker()


# 2. График функции y = x + 1

white = '\x1b[48;5;15m'
stop = '\x1b[0m'
print('\n\n\n#2 график')

def draw_pix(start):
    print((start*3) + (white),' ', stop)


height = 10
width = 10


def graph(h, w):
    for i in range(w, 0, -1):
        draw_pix(' '*i)
graph(height, width)


# 3 задание чарт

white = '\x1b[48;5;15m'
stop = '\033[0m'
file = open("sequence.txt")
file_ms = [float(i) for i in file]
cor_dig = [i for i in file_ms if ((i <= 5) and (i >= -5))]
print(cor_dig)
print(len(cor_dig))
less_0 = len([i for i in cor_dig if (i > 0)])
more_0 = len(cor_dig) - less_0

def draw_line(count):
    print(white*(count < less_0), '  ', stop, ' ',white*(count < more_0), '  ', stop,)

def chart():
    for i in range(max(less_0, more_0), 0, -1):
        draw_line(i)
chart()
print(' <0     >0')

white = '\x1b[48;5;15m'
stop = '\033[0m'


# 4 задание фигурa

white = '\x1b[48;5;15m'
stop = '\033[0m'


def draw_pix(st1, en1, st2, en2):
    ln1 = ' '*(st1-1) + white + ' '*(en1-st1 + 1) + stop
    ln2 = ' '*(st2-1 - en1) + white + ' '*(en2-st2 + 1) + stop
    print(ln1, end='')
    print(ln2)


def fig(size):
    width_of_place = size*4 + 1
    height_of_place = size*2 + 1
    first1 = ((width_of_place // 2) + 1) // 2 + 1
    first2 = first1 + (size*2)
    # draw_pix(first1, first1, first2, first2)
    for i in range(first1):
        # print(first1-i, first1+i, first2-i, first2+i)
        draw_pix(first1-i, first1+i, first2-i, first2+i)
    for i in range(first1, 0, -1):
        # print(first1-i, first1+i, first2-i, first2+i)
        draw_pix(first1-i, first1+i, first2-i, first2+i)
    draw_pix(first1, first1, first2, first2)

fig(5)