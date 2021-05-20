import sys

student_file = 'homework3.py'

f = open(student_file)
lines = f.readlines()
f.close()
lines = [line.strip() for line in lines]
lines = ['' if line.startswith('#') else line for line in lines]
code_clean = True
for i in range(len(lines)):
    if 'import' in lines[i] and not lines[i].endswith('math'):
        print(f'Line {i} of {student_file} contains an import or eval() statement. You must delete this line.')
        code_clean = False
    elif 'input' in lines[i]:
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

from homework3 import *

part = 1
func = calculate_journey_duration
args = [[True, True, True], [True, False, True], [False, True, True], [True, False, False], [False, False, False], ]
expected_return_values = [-1, 4, 7, 2, 1, ]
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
func = break_check_points
args = [[[-1, 5, 9, 4, 3]], [[22, 46, 7, 2]], [[4, 7, 9, 8]], [[-1, -1, -1, -1]], [[8, 6, 7, 3, 5, 9]], [[4, 3, 2, 1]],
        [[10, 11, 12]], [[4]], [[7, 2, -1]], [[4, -1, 8, 9, -1]], ]
expected_return_values = [['N/A', 2, 2, 3, 3, 3, 2, 2, 3], ['N/A', 'N/A', 2, 2, 2, 2],
                          [2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 2], ['N/A', 'N/A', 'N/A', 'N/A'],
                          [2, 2, 2, 3, 3, 2, 2, 2, 3, 2, 2, 3, 3, 3], [2, 2, 3, 2, 1], ['N/A', 'N/A', 'N/A'], [2, 2],
                          [2, 2, 2, 2, 'N/A'], [2, 2, 'N/A', 2, 2, 2, 3, 3, 3, 'N/A'], ]
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
func = check_points_possible
args = [[[3, 2, 8], 4, 6], [[3, 5, 4, 1], 4, 3], [[3, 5, 4, 1], 0, 3], [[3, 5, 4, 1], 4, 0], [[1, 2, 2], 1, 2], [[1, 2, 2], 1, 2], [[9, 6, 10, 1, 7, 10, 9, 8, 5], 1, 13], [[2, 1, 1, 5, 6, 8, 2, 9], 1, 9], [[5, 8, 8, 5], 2, 6], [[7, 2, 5, 7], 3, 7], ]
expected_return_values = [3, 2, 1, 1, 2, 2, 4, 5, 2, 3, ]
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
func = days_for_target
args = [[3040, 3000], [3040, 2980], [3500, 2950], [2940, 2938], [2107, 1969], [2178, 1784], [2834, 2697], [2220, 1790], [3845, 3397], [2078, 1883], ]
expected_return_values = [4, 10, 109, 1, 25, 79, 25, 87, 88, 38, ]
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
func = count_remaining_items
args = [[['Spinach', 'Tomato'], ['Tomato', 'Spinach']], [['Apple', 'Tomato', 'Orange'], ['Tomato', 'Salt', 'Orange']], [['Lettuce', 'Carrot'], ['Orange', 'Apple', 'Carrot']], [['Carrot'], ['Milk', 'Eggs', 'Bread']], [['Carrot', 'Tomato', 'Lettuce'], ['Eggs', 'Yogurt', 'Bread']], [['Cauliflower', 'Pears', 'Avocados', 'Onions', 'Peppers', 'Carrots'], ['Pears', 'Cauliflower', 'Zucchini', 'Carrots']], [['Avocados', 'Radishes', 'Ginger', 'Kale'], ['Onions', 'Zucchini', 'Arugula', 'Mushrooms', 'Ginger', 'Avocados']], [['Avocados'], ['Tomatoes', 'Avocados', 'Garlic', 'Arugula', 'Carrots']], [['Celery', 'Pears', 'Corn', 'Garlic', 'Tuna'], ['Asparagus']], [['Cauliflower', 'Broccoli', 'Lemons', 'Tomatoes', 'Garlic'], ['Tomatoes', 'Potatoes', 'Tuna', 'Zucchini', 'Broccoli']], ]
expected_return_values = [0, 1, 1, 1, 3, 3, 2, 0, 5, 3, ]
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
