#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


def writeCsv():
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


def readCsv():
    with open('names.csv', 'r') as fp:
        reader = csv.reader(fp)
        for name in reader:
            print(name)


def readCsv2():
    with open('names.csv', 'r') as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            print(row['first_name'], row['last_name'])


if __name__ == '__main__':
    # writeCsv()
    readCsv2()
