import sys

student_file = 'lab8.py'

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

part_counts = [0] * 1
test_counts = []

from lab8 import *

part = 1
func = number_of_sets
args = [["Mon", {'Mon': 'Jogging', 'Tue': 'Crunches', 'Wed': 'Jumping Jacks', 'Thu': 'Sit-ups', 'Fri': 'Planks'},
         {'Jogging': 15, 'Crunches': 15, 'Jumping Jacks': 6, 'Sit-ups': 10, 'Planks': 9}],
        ["Tue", {'Mon': 'Jumping Jacks', 'Tue': 'Sit-ups', 'Wed': 'Planks', 'Thu': 'Jogging', 'Fri': 'Leg Presses'},
         {'Jumping Jacks': 17, 'Sit-ups': 7, 'Planks': 5, 'Jogging': 15, 'Leg Presses': 19}],
        ["Mon", {'Mon': 'Jogging', 'Tue': 'Planks', 'Wed': 'Leg Presses', 'Thu': 'Lunges', 'Fri': 'Bench Presses'},
         {'Jogging': 20, 'Planks': 13, 'Leg Presses': 20, 'Lunges': 6, 'Bench Presses': 14}],
        ["Mon", {'Mon': 'Lunges', 'Tue': 'Crunches', 'Wed': 'Jogging', 'Thu': 'Leg Presses', 'Fri': 'Biceps Curls'},
         {'Lunges': 21, 'Crunches': 18, 'Jogging': 20, 'Leg Presses': 21, 'Biceps Curls': 18}],
        ["Sun", {'Mon': 'Leg Presses', 'Tue': 'Jogging', 'Wed': 'Biceps Curls', 'Thu': 'Sit-ups', 'Fri': 'Crunches'},
         {'Leg Presses': 10, 'Jogging': 15, 'Biceps Curls': 15, 'Sit-ups': 17, 'Crunches': 7}], ["Thu",
                                                                                                 {'Mon': 'Sit-ups',
                                                                                                  'Tue': 'Jumping Jacks',
                                                                                                  'Wed': 'Bench Presses',
                                                                                                  'Thu': 'Jogging',
                                                                                                  'Fri': 'Leg Presses'},
                                                                                                 {'Sit-ups': 16,
                                                                                                  'Jumping Jacks': 5,
                                                                                                  'Bench Presses': 16,
                                                                                                  'Jogging': 12,
                                                                                                  'Leg Presses': 17}],
        ["Mon", {'Mon': 'Planks', 'Tue': 'Leg Presses', 'Wed': 'Crunches', 'Thu': 'Jumping Jacks', 'Fri': 'Jogging'},
         {'Planks': 10, 'Leg Presses': 9, 'Crunches': 19, 'Jumping Jacks': 17, 'Jogging': 19}],
        ["Thu", {'Mon': 'Jogging', 'Tue': 'Biceps Curls', 'Wed': 'Bench Presses', 'Thu': 'Sit-ups', 'Fri': 'Lunges'},
         {'Jogging': 18, 'Biceps Curls': 18, 'Bench Presses': 5, 'Sit-ups': 8, 'Lunges': 7}],
        ["Thu", {'Mon': 'Bench Presses', 'Tue': 'Crunches', 'Wed': 'Lunges', 'Thu': 'Planks', 'Fri': 'Jumping Jacks'},
         {'Bench Presses': 5, 'Crunches': 15, 'Lunges': 13, 'Planks': 20, 'Jumping Jacks': 6}], ["Tue", {
        'Mon': 'Jumping Jacks', 'Tue': 'Biceps Curls', 'Wed': 'Leg Presses', 'Thu': 'Planks', 'Fri': 'Crunches'},
                                                                                                 {'Jumping Jacks': 16,
                                                                                                  'Biceps Curls': 12,
                                                                                                  'Leg Presses': 7,
                                                                                                  'Planks': 6,
                                                                                                  'Crunches': 21}], ]
expected_return_values = [4, 8, 3, 2, 0, 5, 6, 7, 3, 5, ]
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
