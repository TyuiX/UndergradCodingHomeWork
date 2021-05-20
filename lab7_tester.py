import sys

student_file = 'lab7.py'

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


def check_float_actual(exp, act):
    if isinstance(act, float):
        print('Actual return value:   {:.3f}'.format(act))
    else:
        print(f'Actual return value:   {act}')
    if isinstance(act, float) and abs(exp - act) <= 0.001:
        print('Correct!')
        return True
    elif not isinstance(act, float):
        print('Incorrect! (wrong value and/or wrong return type)')
        return False
    else:
        print('Incorrect!')
        return False


part_counts = [0] * 1
test_counts = []

from lab7 import *

part = 1
func = check_halves
args = [["abcdefgabcdegf"], ["abcdabcd"], ["aa"], ["a"], ["qwertyuiop"], ["xyx"], ["xxxy"], ["ggggggggggg"], ]
expected_return_values = [5, 4, 1, 0, 0, 0, 1, 5, ]
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
    print(f'Part {i+1}: {part_counts[i]}/{test_counts[i]} tests passed')

#print('\n*** Please note that different test cases will be used during grading! ***')
