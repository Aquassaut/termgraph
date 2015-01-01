#!/usr/bin/env python
# coding=utf-8

# termgraph.py - draw basic graphs on terminal
# https://github.com/mkaz/termgraph

# Marcus Kazmierczak
# http://mkaz.com/

from __future__ import print_function

import argparse
import sys

#TODO: change tick character
tick = '▇'
sm_tick = '|'

# sample bar chart data
#labels = ['2007', '2008', '2009', '2010', '2011']
#data = [183.32, 231.23, 16.43, 50.21, 508.97]

try:
    range = xrange
except NameError:
    pass

def main():

    # determine type of graph
    
    # read data
    labels, data = read_data(args['filename'])

    # verify data
    m = len(labels)
    if m != len(data):
        print(">> Error: Label and data array sizes don't match")
        sys.exit(1)

    # get longest label for padding
    label_max_width = len(max(labels, key=len))

    # massage data
    ## normalize for graph
    max_data = 0
    for i in range(m):
        if data[i] > max_data:
            max_data = data[i]

    step = max_data / args['width']
    # display graph
    for i in range(m):
        print_blocks(labels[i], data[i], step, label_max_width)

    print()


def print_blocks(label, count, step, label_width):
    #TODO: add flag to hide data labels
    blocks = int(count / step)
    print("{{:<{}}}: ".format(label_width).format(label), end="")
    if count < step:
        sys.stdout.write(sm_tick)
    else:
        for i in range(blocks):
            sys.stdout.write(tick)

    print("{:>7.2f}".format(count))


def init():
    parser = argparse.ArgumentParser(description='draw basic graphs on terminal')
    parser.add_argument('filename', nargs='?', default="-", help='data file name (comma or space separated). Defaults to stdin.')
    parser.add_argument('--width', type=int, default=50, help='width of graph in characters default:50')
    parser.add_argument('--verbose', action='store_true')
    args = vars(parser.parse_args())
    return args


def read_data(filename):
    #TODO: add verbose flag
    stdin = filename == '-'

    print("------------------------------------")
    print("Reading data from", ("stdin" if stdin else filename))
    print("------------------------------------\n")

    labels = []
    data = []

    f = sys.stdin if stdin else open(filename, "r")
    for line in f:
        line = line.strip()
        if line:
            if not line.startswith('#'):
                if line.find(",") > 0:
                    cols = line.split(',')
                else:
                    cols = line.split()
                labels.append(cols[0].strip())
                data_point = cols[1].strip()
                data.append(float(data_point))

    f.close()
    return labels, data


if __name__ == "__main__":
    args = init()
    main()



