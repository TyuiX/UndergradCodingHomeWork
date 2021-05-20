import sys

student_file = 'lab11.py'

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


from lab11 import *

part = 1
func = compress_dna_sequence
args = [["TATATAATTATATATA", {'ATAT': 'a', 'TTAA': 'e', 'ATTA': 'g'}], ["TTATATTTTTATTTAT", {'TTAA': 'x', 'AATA': 'y', 'TAAA': 'z', 'AAAT': 'a'}], ["TTTTAATAAAAATAATATTA", {'ATTA': 'q', 'TTTT': 'a', 'TTAT': 'z', 'AAAT': 'x', 'AAAA': 'c', 'TAAT': 'v'}], ["AATAAATAAATAAATAAATAAATA", {'ATTT': 'q', 'TTTT': 'a', 'ATAA': 'z', 'TTAT': 'x', 'TTAA': 'c', 'AATA': 'v'}], ["TTATATTTAAAATAAAAAAAAAAA", {'TTAT': 'g', 'AATA': 'b', 'TAAA': 'n', 'TTTT': 'm', 'ATTT': 'f', 'TTAA': 'g', 'ATAA': 'e'}], ]
expected_return_values = ["agaa", "yzyy", "czaqv", "xxxxxx", "bnmfmm", ]
test_counts.append(len(args))

print('#' * 25 + f' Testing Part {part} ' + '#' * 25)
for arg_list, expected in zip(args, expected_return_values):
    print('Testing ' + func.__name__ + '() with args = ' + ', '.join([str(a) for a in arg_list]))
    print(f'Expected return value: {expected}')
    actual = func(*arg_list)
    print(f'Actual return value:   {actual}')
    if expected == actual:
        part_counts[part - 1] += 1
        print('Correct!')
    else:
        print('Incorrect.')
    print()
print('#' * 66 + '\n')

print('Results:')
for i in range(part):
    print(f'Part {i + 1}: {part_counts[i]}/{test_counts[i]} tests passed')
