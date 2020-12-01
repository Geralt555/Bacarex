#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Дано предложение. Удалить из него все буквы о, стоящие на нечетных местах.

def okiller(mstr):
    res = (''.join(char for n, char in enumerate(
        mstr) if not (char == 'о' and n % 2 == 0)))
    print(res)


if __name__ == '__main__':
    okiller(mstr='Молочную продукцию любят дети')
