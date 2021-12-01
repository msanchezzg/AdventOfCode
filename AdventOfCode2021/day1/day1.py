# -*- coding: utf-8 -*-


import sys
import argparse


def main(input_file):

    with open(input_file, "r") as f:
        lines = f.readlines()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Python3 template file for Advent of Code problems"
    )
    parser.add_argument("input_file", type=str, help="File with problem input")

    args = parser.parse_args()
    main(args.input_file)
