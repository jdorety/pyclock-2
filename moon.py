#!/usr/bin/env python
import unicornhat
pixels = [[(0, 0, 132), (132, 132, 0), (0, 0, 132), (0, 0, 132), (132, 132, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132)], [(0, 0, 132), (0, 0, 132), (0, 0, 132), (132, 132, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132)], [(0, 0, 132), (0, 0, 132), (132, 132, 132), (132, 132, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132)], [(132, 132, 0), (0, 0, 132), (132, 132, 132), (132, 132, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132)], [
    (0, 0, 132), (0, 0, 132), (132, 132, 132), (132, 132, 132), (132, 132, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132)], [(0, 0, 132), (0, 0, 132), (0, 0, 132), (132, 132, 132), (132, 132, 132), (132, 132, 132), (132, 132, 132), (132, 132, 132)], [(0, 0, 132), (132, 132, 0), (0, 0, 132), (0, 0, 132), (132, 132, 132), (132, 132, 132), (132, 132, 132), (0, 0, 132)], [(0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (0, 0, 132), (132, 132, 0)]]


def moon():
    unicornhat.set_pixels(pixels)
    unicornhat.brightness(.5)
    unicornhat.show()
