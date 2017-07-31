#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
migrations = os.path.join(current_dir, 'Migrations')


def grep(filename, string):
    try:
        with open(filename) as f:
            for line in f:
                if string in line:
                    return True
        return False
    except:
        print(filename)
        raise


def get_filepath(path=migrations, match='.sql'):
    filepaths = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            if match in filename:
                filepath = os.path.join(root, filename)
                filepaths.append(filepath)
    return filepaths

if __name__ == '__main__':
    files = get_filepath()
    while True:
        string = input('Введите строку: ')
        files = [file for file in files if grep(file, string)]
        for file in files:
            print(file)
        print('Всего: {}'.format(len(files)))
