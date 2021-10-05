#usr/bin/env python3
# -*- coding: utf-8 -*-
#определите общие символы в двух строках, введенных с клавиатуры.

if __name__ == "__main__":

    a = {1, 2, 3, 8, 11, 125, 13}
    b = {2, 5, 11, 125, 9, 60, 12}
    c = a.intersection(b)
    print(c)
