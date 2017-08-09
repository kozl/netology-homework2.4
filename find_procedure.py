#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
migrations = os.path.join(current_dir, 'Migrations')


def grep(filename, str):
    with open(filename) as f:
        text = f.read()
        if str in text:
            return True
        else:
            return False


def get_filepaths(path=migrations, match='.sql'):
    filepaths = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(match):
                filepath = os.path.join(root, filename)
                filepaths.append(filepath)
    return filepaths

if __name__ == '__main__':
    files = get_filepaths()
    while True:
        str = input('Введите строку: ')
        files = [file for file in files if grep(file, str)]
        for file in files:
            print(file)
        print('Всего: {}'.format(len(files)))
