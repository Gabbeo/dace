#!/usr/bin/env python
import dace as dp

W = dp.symbol('W')
H = dp.symbol('H')


@dp.program
def transpose(input, output):
    @dp.map(_[0:H, 0:W])
    def compute(i, j):
        a << input[j, i]
        b >> output[i, j]
        b = a


@dp.program
def bla(input, output):
    transpose(input, output)


@dp.program
def myprogram(A, B):
    bla(A, B)


if __name__ == '__main__':
    dp.compile(myprogram, dp.float32[W, H], dp.float32[H, W])
