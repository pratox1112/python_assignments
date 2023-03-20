import math
import os
import random
import re
import sys
import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z"
    parsed_t1 = datetime.datetime.strptime(t1, format_string)
    parsed_t2 = datetime.datetime.strptime(t2, format_string)

    diff = parsed_t2 - parsed_t1

    return str(int(abs(diff.total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
