import sys
from hw5_classes import *

student_file = 'homework5.py'

f = open(student_file)
lines = f.readlines()
f.close()
lines = [line.strip() for line in lines]
lines = ['' if line.startswith('#') else line for line in lines]
code_clean = True
for i in range(len(lines)):
    # if 'import' in lines[i] and not lines[i].endswith('math'):
    #     print(f'Line {i} of {student_file} contains an import or eval() statement. You must delete this line.')
    #     code_clean = False
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

part_counts = [0] * 5
test_counts = []

from homework5 import *

part = 1
func = treatment_cost
args = [[Hospital(10, 4, 3, 1000, 1200), ('p1', 67, False)], [Hospital(10, 4, 3, 1000, 1200), ('p1', 45, False)], [Hospital(10, 4, 3, 1000, 1200), ('p1', 45, True)], [Hospital(10, 4, 3, 1000, 1200), ('p1', 76, True)], [Hospital(10, 4, 3, 1200, 1400), ('p1', 76, True)], [Hospital(10, 7, 5, 800, 1400), ('p1', 41, True)], [Hospital(10, 8, 9, 900, 1500), ('p1', 56, True)], [Hospital(10, 6, 6, 700, 1800), ('p1', 56, True)], [Hospital(13, 6, 5, 800, 1100), ('p1', 91, True)], [Hospital(19, 8, 5, 500, 1500), ('p1', 81, True)], [Hospital(17, 5, 5, 500, 2000), ('p1', 44, True)], [Hospital(12, 5, 7, 800, 1900), ('p1', 65, True)], [Hospital(14, 8, 5, 700, 1500), ('p1', 68, True)], [Hospital(17, 6, 9, 1000, 1800), ('p1', 71, True)], [Hospital(15, 5, 8, 1000, 1800), ('p1', 62, True)], ]
expected_return_values = [1000, 0, 1000, 2200, 2600, 800, 900, 700, 1900, 2000, 500, 800, 700, 1000, 1000, ]
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
func = find_remaining_ventilators
args = [[Hospital(10, 4, 3, 1000, 1200), [('p1', 45, False), ('p2', 61, False), ('p3', 76, True)]], [Hospital(10, 4, 3, 1000, 1200), [('p1', 45, False), ('p2', 77, True), ('p3', 76, True)]], [Hospital(10, 4, 3, 1000, 1200), [('p1', 45, False), ('p2', 61, False), ('p3', 76, False)]], [Hospital(10, 1, 3, 1000, 1200), [('p1', 45, False), ('p2', 61, False), ('p3', 76, False)]], [Hospital(10, 2, 5, 1000, 1200), [('p1', 45, False), ('p2', 61, False), ('p3', 76, False)]], [Hospital(10, 7, 5, 800, 1400), [('p1', 88, True), ('p1', 92, True), ('p1', 90, True)]], [Hospital(10, 8, 9, 900, 1500), [('p1', 89, True), ('p1', 38, True), ('p1', 45, True), ('p1', 43, True), ('p1', 56, True)]], [Hospital(18, 7, 10, 600, 1200), [('p1', 92, True), ('p1', 62, True), ('p1', 84, True)]], [Hospital(11, 9, 8, 500, 1000), [('p1', 81, True), ('p1', 63, True), ('p1', 41, True), ('p1', 92, True), ('p1', 37, True)]], [Hospital(11, 10, 6, 600, 1000), [('p1', 93, True), ('p1', 62, True), ('p1', 71, True), ('p1', 65, True), ('p1', 51, True)]], [Hospital(17, 5, 7, 700, 1800), [('p1', 48, True), ('p1', 87, True), ('p1', 73, True), ('p1', 75, True), ('p1', 68, True), ('p1', 71, True)]], [Hospital(15, 5, 8, 1000, 1800), [('p1', 78, True), ('p1', 69, True), ('p1', 75, True), ('p1', 85, True), ('p1', 77, True), ('p1', 73, True)]], [Hospital(17, 9, 10, 800, 1500), [('p1', 89, True), ('p1', 83, True), ('p1', 76, True)]], [Hospital(12, 10, 5, 800, 2000), [('p1', 45, True), ('p1', 56, True), ('p1', 56, True), ('p1', 70, True), ('p1', 60, True)]], [Hospital(11, 10, 8, 800, 1900), [('p1', 36, True), ('p1', 47, True), ('p1', 72, True), ('p1', 40, True), ('p1', 88, True)]], ]
expected_return_values = [3, 2, 4, 1, 2, 4, 7, 5, 7, 9, 4, 2, 6, 10, 9, ]
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
func = find_hospitalization_count
args = [[Hospital(10, 4, 3, 1000, 1200), [('p1', 45, False), ('p2', 61, False), ('p3', 76, True)]], [Hospital(10, 4, 3, 1000, 1200), [('p1', 66, False), ('p2', 77, True), ('p3', 76, True)]], [Hospital(10, 2, 2, 1000, 1200), [('p1', 66, False), ('p2', 77, False), ('p3', 76, True)]], [Hospital(10, 4, 3, 1000, 1200), [('p1', 26, False), ('p2', 28, False), ('p3', 45, False)]], [Hospital(10, 4, 4, 1000, 1200), [('p1', 77, True), ('p2', 79, True), ('p3', 76, True)]], [Hospital(10, 7, 5, 800, 1400), [('p1', 88, True), ('p1', 92, True), ('p1', 90, True)]], [Hospital(10, 8, 9, 900, 1500), [('p1', 89, True), ('p1', 38, True), ('p1', 45, True), ('p1', 43, True), ('p1', 56, True)]], [Hospital(18, 7, 10, 600, 1200), [('p1', 92, True), ('p1', 62, True), ('p1', 84, True)]], [Hospital(11, 9, 8, 500, 1000), [('p1', 81, True), ('p1', 63, True), ('p1', 41, True), ('p1', 92, True), ('p1', 37, True)]], [Hospital(11, 10, 6, 600, 1000), [('p1', 93, True), ('p1', 62, True), ('p1', 71, True), ('p1', 65, True), ('p1', 51, True)]], [Hospital(17, 5, 7, 700, 1800), [('p1', 48, True), ('p1', 87, True), ('p1', 73, True), ('p1', 75, True), ('p1', 68, True), ('p1', 71, True)]], [Hospital(15, 5, 8, 1000, 1800), [('p1', 78, True), ('p1', 69, True), ('p1', 75, True), ('p1', 85, True), ('p1', 77, True), ('p1', 73, True)]], [Hospital(17, 9, 10, 800, 1500), [('p1', 89, True), ('p1', 83, True), ('p1', 76, True)]], [Hospital(12, 10, 5, 800, 2000), [('p1', 45, True), ('p1', 56, True), ('p1', 56, True), ('p1', 70, True), ('p1', 60, True)]], [Hospital(11, 10, 8, 800, 1900), [('p1', 36, True), ('p1', 47, True), ('p1', 72, True), ('p1', 40, True), ('p1', 88, True)]], ]
expected_return_values = [0, 1, 2, 0, 0, 0, 4, 1, 3, 4, 5, 3, 0, 5, 4, ]
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
func = hospital_accommodation_count
args = [[Hospital(5, 4, 3, 800, 1400)], [Hospital(6, 8, 3, 800, 1800)], [Hospital(10, 4, 3, 600, 1200)], [Hospital(10, 6, 5, 1000, 1300)], [Hospital(7, 2, 6, 500, 1900)], [Hospital(11, 2, 3, 700, 1700)], [Hospital(6, 2, 3, 1000, 1200)], [Hospital(7, 8, 3, 700, 1600)], [Hospital(12, 4, 6, 500, 1400)], [Hospital(10, 6, 6, 600, 1900)], [Hospital(10, 2, 6, 1000, 1800)], [Hospital(11, 7, 7, 1000, 2000)], [Hospital(12, 6, 8, 800, 1500)], [Hospital(5, 8, 8, 600, 1100)], [Hospital(12, 7, 5, 600, 1500)], ]
expected_return_values = [4, 8, 4, 6, 2, 2, 2, 8, 4, 6, 2, 7, 6, 8, 7, ]

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
func = non_admittable_treatable_count
args = [[Hospital(3, 1, 5, 1000, 1200), [('p1', 66, False), ('p2', 77, True), ('p3', 76, True), ('p4', 80, True), ('p5', 45, True)]], [Hospital(3, 1, 5, 1000, 1200), [('p1', 66, True), ('p2', 77, True), ('p3', 76, True), ('p4', 80, True), ('p5', 45, True)]], [Hospital(3, 2, 5, 1000, 1200), [('p1', 66, False), ('p6', 68, False), ('p2', 67, True), ('p3', 76, True), ('p4', 80, True), ('p5', 45, True)]], [Hospital(3, 0, 5, 1000, 1200), [('p1', 66, False), ('p6', 68, False), ('p2', 67, True), ('p3', 76, True), ('p4', 80, True), ('p5', 45, True)]], [Hospital(3, 2, 1, 800, 1400), [('p1', 88, True), ('p1', 92, True), ('p1', 90, True), ('p1', 37, True)]], [Hospital(6, 3, 3, 700, 1500), [('p1', 45, True), ('p1', 43, True), ('p1', 56, True)]], [Hospital(7, 2, 3, 600, 1200), [('p1', 92, True), ('p1', 62, True), ('p1', 84, True)]], [Hospital(3, 3, 2, 500, 1000), [('p1', 81, True), ('p1', 63, True), ('p1', 41, True), ('p1', 92, True), ('p1', 37, True), ('p1', 40, True), ('p1', 77, True), ('p1', 44, True)]], [Hospital(4, 1, 2, 800, 1900), [('p1', 51, True), ('p1', 65, True), ('p1', 88, True), ('p1', 37, True), ('p1', 84, True), ('p1', 54, True), ('p1', 56, True), ('p1', 68, True), ('p1', 86, True), ('p1', 65, True)]], [Hospital(4, 3, 3, 900, 1900), [('p1', 35, True), ('p1', 60, True), ('p1', 92, True), ('p1', 84, True), ('p1', 76, True), ('p1', 67, True), ('p1', 62, True), ('p1', 78, True)]], [Hospital(7, 3, 3, 900, 1700), [('p1', 58, True), ('p1', 67, True), ('p1', 37, True), ('p1', 89, True), ('p1', 83, True), ('p1', 76, True), ('p1', 46, True), ('p1', 81, True), ('p1', 87, True)]], [Hospital(3, 2, 3, 700, 1200), [('p1', 56, True), ('p1', 70, True), ('p1', 60, True), ('p1', 91, True), ('p1', 39, True), ('p1', 81, True), ('p1', 64, True), ('p1', 59, True)]], [Hospital(7, 2, 1, 600, 1900), [('p1', 88, True), ('p1', 75, True), ('p1', 58, True), ('p1', 35, True)]], [Hospital(5, 1, 2, 900, 1800), [('p1', 75, True), ('p1', 53, True), ('p1', 66, True)]], [Hospital(4, 3, 2, 600, 1200), [('p1', 59, True), ('p1', 83, True), ('p1', 64, True), ('p1', 37, True), ('p1', 35, True), ('p1', 43, True), ('p1', 64, True), ('p1', 47, True), ('p1', 36, True), ('p1', 51, True)]], ]
expected_return_values = [2, 2, 3, 3, 1, 0, 0, 5, 6, 4, 2, 5, 0, 0, 6, ]

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
