# Jason Zhang
# jasozhang
# 112710259
# CSE 101
# Lab Assignment 12

import re

def find_university_emails(emails):
    pattern = r'^[a-zA-Z]{1,}[@][a-zA-Z]{1,}(.edu)$'
    x = []
    for i in emails:
        y = re.match(pattern, i)
        if y:
            x.append(i)
    return x

