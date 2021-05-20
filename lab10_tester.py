import sys

student_file = 'lab10.py'

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


def verify_points(points, points_selected):
    if len(points) != len(points_selected):
        return False
    for ind in range(len(points)):
        if points[ind] != points_selected[ind]:
            return False
    return True


from lab10 import *

part = 1
func = find_above_avg_players
args = [[Team('NY Giants', [Player('B', 8), Player('D', 13), Player('A', 1), Player('C', 2)])],
        [Team('NY Jets', [Player('A', 12), Player('E', 10), Player('D', 10), Player('C', 17), Player('F', 1), Player('B', 17)])],
        [Team('LA Lakers', [Player('C', 0), Player('A', 7), Player('B', 5)])],
        [Team('Atlanta Braves', [Player('F', 14), Player('B', 12), Player('E', 10), Player('D', 0), Player('H', 1), Player('A', 19), Player('G', 3), Player('I', 2), Player('C', 2)])],
        [Team('Detroit Tigers', [Player('G', 15), Player('B', 15), Player('C', 1), Player('H', 6), Player('E', 10), Player('D', 9), Player('A', 8), Player('F', 16)])], ]
expected_return_values = [[Player('B', 8), Player('D', 13)],
                          [Player('A', 12), Player('C', 17), Player('B', 17)],
                          [Player('A', 7), Player('B', 5)],
                          [Player('F', 14), Player('B', 12), Player('E', 10), Player('A', 19)],
                          [Player('G', 15), Player('B', 15), Player('E', 10), Player('F', 16)], ]
test_counts.append(len(args))

print('#' * 25 + f' Testing Part {part} ' + '#' * 25)
for arg_list, expected in zip(args, expected_return_values):
    print('Testing ' + func.__name__ + '() with args = ' + ', '.join([str(a) for a in arg_list]))
    expected = sorted(expected)
    print(f'Expected return value: {expected}')
    actual = func(*arg_list)
    actual = sorted(actual) if isinstance(actual, list) else actual
    print(f'Actual return value:   {actual}')
    if verify_players(expected, actual):
        part_counts[part - 1] += 1
    print()
print('#' * 66 + '\n')

print('Results:')
for i in range(part):
    print(f'Part {i + 1}: {part_counts[i]}/{test_counts[i]} tests passed')
