import sys


def collatz(number):
    even = number // 2
    odd = 3 * number + 1
    while number > 0:
        if number % 2 == 0:
            print(even)
            if even == 1:
                sys.exit()
            else:
                collatz(even)
        else:
            number % 2 == 1
            if odd == 1:
                print(odd)
                sys.exit()
            else:
                print(odd)
                collatz(odd)


print("Input number below")
try:
    collatz(int(input('')))
except ValueError:
    print('You must enter an integer.')
