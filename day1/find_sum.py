"""
find_sum.py

Given the list `input.txt`, find the two entries whose sum is equal to 2020,
e.g.

    > n1 + n2 = 2020

Give your response to the puzzle as the product of these two numbers, for
example:

    > ans = n1 * n2

Author: Sam Foreman
Date: 12/1/2020
"""
import os
import numpy as np


def find_two_entries(arr, goal=2020):
    num_entries = len(arr)
    for i in range(num_entries):
        for j in range(i, num_entries):
            tot = arr[i] + arr[j]
            if tot == goal:
                return arr[i] * arr[j]


def find_three_entries(arr, goal=2020):
    num_entries = len(arr)
    for i in range(num_entries):
        for j in range(i, num_entries):
            for k in range(j, num_entries):
                tot = arr[i] + arr[j] + arr[k]
                if tot == goal:
                    return arr[i] * arr[j] * arr[k]








