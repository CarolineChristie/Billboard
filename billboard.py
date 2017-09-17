#!/usr/bin/python3

##########################################
# Author: Caroline Christie
# Date: Sept 17 2017
# Description: This script outputs the maximum possible font size for a billboard,
# given the height, width, and text desired.
# This script was written with Python 3.6 and not tested with any previous versions.
# It also uses the optional Python type annotations
#
# Usage: python3 billboard.py <filename to process>
#
# Input files should be in the following format:
# <Number of cases>
# <Width> <Height> <Text>
# Maximum width and height are 1000.
#
# Input:
# 5
# 20 6 hacker cup
# 100 20 hacker cup 2013
# 10 20 MUST BE ABLE TO HACK
# 55 25 Can you hack
# 100 20 Hack your way to the cup
#
# Output:
# Case #1: 3
# Case #2: 10
# Case #3: 2
# Case #4: 8
# Case #5: 7
#
##########################################

import sys


def is_next_char_a_space(cur_pos: int, text: str) -> bool:
    if cur_pos >= len(text) or text[cur_pos] == " ":
        return True
    else:
        return False


def max_characters(font_size: int, width: int) -> int:
    max_ch = width // font_size
    return max_ch


def is_too_tall(font_size: int, height: int, nbr_lines: int) -> bool:
    if nbr_lines * font_size > height:
        return True
    else:
        return False


def wrap_text(width: int, font_size: int, text: str) -> list:
    lines = []
    while text != "":
        for cur_pos in range(max_characters(font_size, width), -1, -1):
            if is_next_char_a_space(cur_pos, text):
                line = text[: cur_pos]
                lines.append(line)
                text = text[cur_pos + 1:]
                break
        if len(lines) is 0 or cur_pos is 0:
            return []
    return lines


def get_max_fontsize(width: int, height: int, text: str) -> int:
    for fontsize in range(1, 1002):  # max fontsize is 1000, to reach 1000 we need to test 1001 values.
        lines = wrap_text(width, fontsize, text)
        if is_too_tall(fontsize, height, len(lines)) or len(lines) is 0:
            # if lines is empty, then the longest word was too wide.
            return fontsize - 1


def process_file(filename: str) -> None:
    with open(filename, "r") as input:
        lines = input.read().splitlines()
        number_of_cases = int(lines[0])
        for case in range(1, number_of_cases + 1):
            data = lines[case].split(" ", 2)
            width = int(data[0])
            height = int(data[1])
            text = data[2]
            print("Case #{}: {}".format(str(case), str(get_max_fontsize(width, height, text))))


process_file(sys.argv[1])
