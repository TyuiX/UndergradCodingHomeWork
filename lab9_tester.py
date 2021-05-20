import sys

student_file = 'lab9.py'

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


def verify_points(correct_coordinates, points_selected):
    if points_selected is None:
        return False
    points = [Point(x, y) for x, y in correct_coordinates]
    if len(points) != len(points_selected):
        return False
    for ind in range(len(points)):
        if points[ind] != points_selected[ind]:
            return False
    return True


from lab9 import *

part = 1
func = find_points_on_line
args = [[[(0, -1), (1, 1), (2, 1)], 2, -1], [[(1, 1), (2, 2), (2, -1)], 1, 0], [[(1, 2), (1, 3), (2, 4), (3, 1)], 2, 0],
        [[(2, 1), (3, 4), (4, 2), (5, 6)], 0, 1], [[(1, 2), (2, 3), (2, 1), (4, 2)], 1, 1], ]
expected_return_values = [[(0, -1), (1, 1)], [(1, 1), (2, 2)], [(1, 2), (2, 4)], [(2, 1)], [(1, 2), (2, 3)], ]
test_counts.append(len(args))

print('#' * 25 + f' Testing Part {part} ' + '#' * 25)
for arg_list, expected in zip(args, expected_return_values):
    print('Testing ' + func.__name__ + '() with args = ' + ', '.join([str(a) for a in arg_list]))
    print(f'Expected return value: {expected}')
    actual = func(*arg_list)
    print(f'Actual return value:   {actual}')
    if verify_points(expected, actual):
        part_counts[part - 1] += 1
    print()
print('#' * 66 + '\n')

print('Results:')
for i in range(part):
    print(f'Part {i + 1}: {part_counts[i]}/{test_counts[i]} tests passed')
