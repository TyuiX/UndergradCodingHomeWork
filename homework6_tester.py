import sys

student_file = 'homework6.py'

f = open(student_file)
lines = f.readlines()
f.close()
lines = [line.strip() for line in lines]
lines = ['' if line.startswith('#') else line for line in lines]
code_clean = True
for i in range(len(lines)):
    if 'import' in lines[i] and not lines[i].endswith('re'):
        print(f'Line {i} of {student_file} contains an import or eval() statement. You must delete this line.')
        code_clean = False
    if 'input' in lines[i]:
        print(f'Line {i} of {student_file} contains an input() statement. You must delete this line.')
        code_clean = False
    elif 'open' in lines[i]:
        print(f'Line {i} of {student_file} contains an open() statement. You must delete this line.')
        code_clean = False
    elif 'exit' in lines[i] or 'sys.exit' in lines[i]:
        print(f'Line {i} of {student_file} contains an exit() statement. You must delete this line.')
        code_clean = False

if not code_clean:
    print('Your ' + student_file + ' file contains one or more invalid lines of code.')
    print('You will need to remove them before running the driver.')
    print('Note that the presence of those lines renders your work ungradeable!')
    sys.exit()

part_counts = [0] * 8
test_counts = []

from homework6 import *

part = 1
func = find_special_tokens
args = [[['asd', '123', 'a543', 'av123']], [['Ad123', 'XZW12345', 'SBU']], [['aa136', 'a12345', 'af555', 'h99']], [['za782', 'xcz8273', 'gg145', 'A82', 'af231', 'h99']], [['a162', 'a1345', 'af58', 'h9']], ]
expected_return_values = [[3], [], [0, 2], [0, 2, 4], [2], ]
test_counts.append(len(args))

print('#' * 25 + f' Testing Part {part} ' + '#' * 25)
for arg_list, expected in zip(args, expected_return_values):
    print('Testing ' + func.__name__ + '() with args = ' + ', '.join([str(a) for a in arg_list]))
    print(f'Expected return value: {expected}')
    actual = func(*arg_list)
    print(f'Actual return value:   {actual}')
    if expected == actual:
        part_counts[part - 1] += 1
    print()
print('#' * 66 + '\n')



part += 1
func = find_suitable_names
args = [[['none', 'nope', 'nada', 'yayy']], [['1234', 'XZW12345', 'SBU']], [['bonk', 'apple', 'Zapp', 'h99']], [['aa132', '1er4', 'a12345', 'A82', 'Zzzzz', 'h99']], [['Good', 'Bad', 'af23', 'AaaK']], ]
expected_return_values = [['yayy'], [], ['bonk', 'Zapp'], ['1er4'], ['Good', 'AaaK'], ]
test_counts.append(len(args))

print('#' * 25 + f' Testing Part {part} ' + '#' * 25)
for arg_list, expected in zip(args, expected_return_values):
    print('Testing ' + func.__name__ + '() with args = ' + ', '.join([str(a) for a in arg_list]))
    print(f'Expected return value: {expected}')
    actual = func(*arg_list)
    print(f'Actual return value:   {actual}')
    if expected == actual:
        part_counts[part - 1] += 1
    print()
print('#' * 66 + '\n')


part += 1
func = math_expr
args = [[['+99 / +15', '-100 ^   -2', '-13 - -33']], [[]], [['- 15/-12', '-19 + 12', '+12  -  +102', '+3 + +3', '3 + 3', '-3 + -3']], [['', '+Nine - -One', '12 * +12', '-14 -- -15', '-12 - 12']], [['-100      * -1']], ]
expected_return_values = [[0, 1, 2], [], [2, 3, 5], [], [0], ]
test_counts.append(len(args))

print('#' * 25 + f' Testing Part {part} ' + '#' * 25)
for arg_list, expected in zip(args, expected_return_values):
    print('Testing ' + func.__name__ + '() with args = ' + ', '.join([str(a) for a in arg_list]))
    print(f'Expected return value: {expected}')
    actual = func(*arg_list)
    print(f'Actual return value:   {actual}')
    if expected == actual:
        part_counts[part - 1] += 1
    print()
print('#' * 66 + '\n')


part += 1
func = remove_italics
args = [["I <i>love</i> SBU, yes I do!"], ["Hey <i>Wolfie</i>, he's so fine, we hug him <i>all the time</i>!"], ["This text has no italics tags."], ["<i>All of this text is italicized.</i>"], ["<i>beep</i><i>bop</i><i>boop</i><i>bonk</i>"], ]
expected_return_values = ["I love love SBU, yes I do!", "Hey Wolfie Wolfie, he's so fine, we hug him all the time all the time!", "This text has no italics tags.", "All of this text is italicized. All of this text is italicized.", "beep beepbop bopboop boopbonk bonk", ]
test_counts.append(len(args))

print('#' * 25 + f' Testing Part {part} ' + '#' * 25)
for arg_list, expected in zip(args, expected_return_values):
    print('Testing ' + func.__name__ + '() with args = ' + ', '.join([str(a) for a in arg_list]))
    print(f'Expected return value: {expected}')
    actual = func(*arg_list)
    print(f'Actual return value:   {actual}')
    if expected == actual:
        part_counts[part - 1] += 1
    print()
print('#' * 66 + '\n')


part += 1
func = scramble
args = [["AMAZON", "IAKSMDJXUAJWJEHCBZ", 2], ["IPHONE", "JZIANEUDHCZOANZ", 3], ["SCRAMBLEDEGG", "AHXBIAJNPE", 3], ["RANDOM", "RMBC", 6], ["CARWASH", "SOAP", 5], ]
expected_return_values = ["IAAKSMMDAJXZUAOJWN", "JZIIANEPUDHHCZOOANZNJZIE", "AHXSBIACJNPREAHAXBIMAJNBPEALHXBEIAJDNPEEAHXGBIAG", "RMBCRMRBCRMBCARMBCRMNBCRMBCDRMBCRMOBCRMBCM", "SOAPSCOAPSOAAPSOARPSOAPWSOAPSAOAPSOSAPSOAH", ]
test_counts.append(len(args))

print('#' * 25 + f' Testing Part {part} ' + '#' * 25)
for arg_list, expected in zip(args, expected_return_values):
    print('Testing ' + func.__name__ + '() with args = ' + ', '.join([str(a) for a in arg_list]))
    print(f'Expected return value: {expected}')
    actual = func(*arg_list)
    print(f'Actual return value:   {actual}')
    if expected == actual:
        part_counts[part - 1] += 1
    print()
print('#' * 66 + '\n')


part += 1
func = unscramble
args = [["IAAKSMMDAJXZUAOJWN", 2], ["JZIIANEPUDHHCZOOANZNJZIE", 3], ["AHXSBIACJNPREAHAXBIMAJNBPEALHXBEIAJDNPEEAHXGBIAG", 3], ["RMBCRMRBCRMBCARMBCRMNBCRMBCDRMBCRMOBCRMBCM", 6], ["SOAPSCOAPSOAAPSOARPSOAPWSOAPSAOAPSOSAPSOAH", 5], ]
expected_return_values = ["AMAZON", "IPHONE", "SCRAMBLEDEGG", "RANDOM", "CARWASH", ]
test_counts.append(len(args))

print('#' * 25 + f' Testing Part {part} ' + '#' * 25)
for arg_list, expected in zip(args, expected_return_values):
    print('Testing ' + func.__name__ + '() with args = ' + ', '.join([str(a) for a in arg_list]))
    print(f'Expected return value: {expected}')
    actual = func(*arg_list)
    print(f'Actual return value:   {actual}')
    if expected == actual:
        part_counts[part - 1] += 1
    print()
print('#' * 66 + '\n')



part += 1
func = cafe_day
args = [[['A', 4, 4, 0], ['S', 2, 8, 0], ['S', 0, 8, 4, 11], ['S', 2, 0, 6]], [['G', 4, 2, 10], ['S', 4, 0, 9], ['D', 5, 0, 4], ['G', 1, 6, 7], ['P', 1], ['G', 1, 6, 4], ['B', 5, 0, 13], ['G', 4, 5, 11], ['P', 0, 1, 4]], [['G', 2, 10, 8], ['P', 4, 6, 11], ['G', 0, 2, 3]], [['S', 1, 7, 0], ['G', 1, 6, 7], ['G', 5, 10, -17], ['P', 3, 10, 15], ['S', 4, 8, 8]], [['S', 4, 1, 8]], [['G', 3, 3, 7], ['S', 2, 1, 12], ['S', 5, 6, 12], ['P', 5, 6, 1], ['P'], ['G', 4, 6, 11], ['G', 3, 0, 0]], [['G', 3, 10, 5, 3], ['P'], ['P', 1, 6, 1], ['G', 5, 1, 4], ['G', 5, 6, 10], ['G', 5, 3, 15], ['G', 5, 6, 11], ['S', 5]], [['P', 5, 7, 8], ['S', 1, 7, 15], ['G', 0, 9, 6], ['S', 4, 5, 10], ['G', 0, 2, 3], ['G', 3, 3, 7]], [['G', 4], ['S', 2, 1, 12], ['G', 5, 9, 3]], [['G', 4, 6, 11], ['P', 0], ['G', 3, 3, 9], ['G', 0, 10, 4]], [['B', 1, 1, 14], ['G', 1, 9, 1], ['G', 3, 10, 14], ['P', 0, 0, 2], ['G', 0, 4, 4]], [['P', 2, 8, 5], ['S', 4, 0, 10], ['S', 4], ['P', 1, 5, 13], ['G', 1, 6, 4], ['P', 1, 8, 14], ['G', 3, 10, 5, 3], ['S', 5, 0, 15], ['P', 5, 7, 12]], [['P', 4, 6, 2], ['S', 5, 6, 11]], [['G', 1, 1, 4], ['P', 1, 3, 7], ['G', 1, 6, 7], ['P', 3, 5, 4], ['P', 4, 6, 2], ['S', 4, 1, 3]], [['D', 0, 7, 6]], [['G', 0, 9, 12], ['G', 5, 6, 0], ['S', 5, 2, 6], ['G', 0, 0, 12], ['S', 2, 8, 0], ['P', 4, 1, 12], ['P', 1, 8, 14], ['G', 0, 9, 8], ['P', 4, 1, -5]], [['S', 3, 3, 2], ['S', 0, 1, 13], ['E', 4, 0, 6], ['G', 5, 1, 4], ['S', 0, 10, 6], ['P', 5, 0, 9], ['S', 4, 1, 3], ['S', 5, 6, 12], ['S', 5, 2, 6]], [['S', 1, 6, 2], ['P', 0, 5, 14], ['G', 0, 4, 4], ['S', 0, 1, 13], ['S', 3, 3, 2], ['G', 2, 2, 8], ['P', 2, 1, 13]], [['S', 0, 10, 11]], [[]], ]
expected_return_values = [40.67, 130.245, 81.35, 136.0, 25.97, 169.16, 146.5, 172.57500000000002, 59.01, 81.60000000000001, 81.7, 221.795, 74.32499999999999, 125.645, 0.0, 214.86, 211.10999999999999, 143.645, 37.975, 0.0, ]
test_counts.append(len(args))

print('#' * 25 + f' Testing Part {part} ' + '#' * 25)
for arg_list, expected in zip(args, expected_return_values):
    print('Testing ' + func.__name__ + '() with args = ' + ', '.join([str(a) for a in arg_list]))
    print(f'Expected return value: {expected}')
    actual = func(arg_list)
    print(f'Actual return value:   {actual}')
    if actual is not None and abs(expected - actual) <= 0.01:
        part_counts[part - 1] += 1
    print()
print('#' * 66 + '\n')



part += 1
func = blackjack_dice
args = [[[1, 1, 3, 1, 6, 1, 4, 2, 6, 1, 3, 3, 2, 1, 3, 1, 4, 1, 2, 3, 6, 1, 1, 5, 1, 6, 4, 2, 6, 5]], [[3, 5, 2, 4, 4, 5, 2, 3, 5, 4, 5, 4, 4, 6, 3, 5, 3, 1, 5, 2, 5, 6, 4, 2, 3, 3, 1, 3, 4, 3]], [[2, 1, 4, 1, 3, 2, 4, 5, 6, 4, 6, 6, 4, 2, 3, 2, 6, 3, 5, 1, 1, 2, 2, 3, 2, 3, 3, 1, 1, 3]], [[1, 3, 1, 4, 1, 5, 3, 6, 2, 3, 5, 3, 3, 4, 6, 6, 3, 5, 5, 3, 2, 1, 6, 1, 4, 4, 1, 4, 6, 5]], [[3, 1, 6, 4, 4, 5, 3, 1, 1, 5, 3, 6, 5, 6, 5, 2, 5, 1, 4, 6, 4, 1, 4, 4, 3, 6, 3, 2, 4, 2]], [[2, 3, 6, 1, 2, 2, 6, 6, 2, 4, 1, 2, 3, 4, 6, 5, 4, 5, 3, 5, 5, 2, 5, 4, 3, 3, 2, 4, 1, 4]], [[6, 5, 4, 3, 5, 1, 1, 6, 3, 5, 3, 3, 5, 3, 5, 5, 2, 6, 1, 3, 4, 5, 2, 4, 3, 6, 1, 2, 5, 2]], [[6, 1, 3, 1, 4, 6, 2, 4, 2, 3, 4, 2, 5, 4, 6, 2, 6, 2, 1, 4, 5, 3, 1, 6, 1, 6, 6, 2, 6, 3]], [[6, 6, 5, 2, 4, 6, 2, 3, 5, 1, 2, 2, 3, 3, 4, 3, 1, 1, 4, 5, 6, 6, 2, 6, 3, 2, 1, 3, 4, 2]], [[2, 6, 1, 6, 3, 5, 1, 4, 5, 3, 3, 3, 2, 2, 2, 1, 6, 1, 6, 1, 4, 4, 1, 6, 5, 6, 3, 2, 2, 1]], [[5, 5, 2, 1, 3, 1, 2, 2, 4, 3, 4, 3, 6, 3, 1, 1, 5, 6, 1, 3, 6, 4, 1, 4, 2, 2, 6, 1, 5, 5]], [[4, 2, 1, 5, 6, 2, 1, 3, 6, 1, 5, 1, 1, 1, 3, 6, 4, 1, 1, 3, 1, 5, 3, 6, 5, 5, 2, 3, 5, 1]], [[1, 2, 3, 5, 5, 1, 1, 6, 2, 1, 5, 5, 4, 5, 6, 6, 2, 3, 6, 3, 4, 6, 6, 4, 3, 5, 1, 3, 5, 4]], [[1, 5, 4, 3, 1, 4, 5, 2, 4, 1, 2, 3, 5, 2, 6, 6, 1, 1, 5, 5, 6, 5, 5, 3, 1, 6, 4, 2, 6, 1]], [[1, 2, 1, 3, 4, 4, 4, 1, 4, 6, 2, 5, 4, 5, 4, 3, 2, 1, 1, 1, 5, 6, 5, 6, 3, 5, 5, 1, 1, 2]], [[6, 5, 1, 6, 2, 2, 2, 6, 5, 1, 1, 5, 3, 4, 4, 4, 2, 2, 4, 5, 3, 1, 1, 2, 6, 3, 3, 3, 6, 5]], [[1, 4, 4, 6, 1, 4, 2, 4, 5, 3, 4, 3, 6, 6, 1, 1, 4, 2, 1, 5, 1, 4, 1, 5, 6, 5, 6, 4, 3, 2]], [[4, 6, 4, 1, 1, 1, 5, 1, 5, 4, 3, 3, 2, 3, 2, 4, 4, 4, 6, 6, 6, 4, 1, 5, 6, 4, 3, 4, 4, 5]], [[3, 3, 5, 3, 4, 2, 4, 4, 4, 5, 3, 2, 3, 4, 3, 3, 3, 2, 1, 4, 1, 4, 6, 4, 5, 5, 3, 4, 2, 4]], [[4, 4, 2, 6, 2, 6, 3, 5, 1, 3, 2, 2, 6, 2, 4, 4, 5, 1, 2, 6, 4, 2, 3, 5, 1, 2, 3, 4, 1, 2]], ]
expected_return_values = [[0, 0], [2, 20], [1, 18], [1, 15], [1, 19], [2, 19], [1, 17], [2, 21], [2, 7], [2, 20], [1, 21], [1, 21], [1, 12], [2, 19], [1, 21], [1, 21], [1, 18], [1, 21], [1, 21], [0, 0], ]
test_counts.append(len(args))

print('#' * 25 + f' Testing Part {part} ' + '#' * 25)
for arg_list, expected in zip(args, expected_return_values):
    print('Testing ' + func.__name__ + '() with args = ' + ', '.join([str(a) for a in arg_list]))
    print(f'Expected return value: {expected}')
    actual = func(*arg_list)
    print(f'Actual return value:   {actual}')
    if expected == actual:
        part_counts[part - 1] += 1
    print()
print('#' * 66 + '\n')



print('Results:')
for i in range(part):
    print(f'Part {i + 1}: {part_counts[i]}/{test_counts[i]} tests passed')

print('\n*** Please note that different test cases will be used during grading! ***')
