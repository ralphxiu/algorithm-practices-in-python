#!/bin/python3

import sys

time = input().strip()

def timeFormatConvert(time):
    if time[-2:] == 'AM':
        if time[:2] == '12':
            return '00' + time[2:-2]
        return time[:-2]
    if time[-2:] == 'PM':
        if time[:2] == '12':
            return time[:-2]
        return (':').join([str(int(x) + 12) if idx == 0 else x for idx, x in enumerate(time[:-2].split(':'))])

print(timeFormatConvert(time))