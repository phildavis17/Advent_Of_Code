import re

TEST_DATA = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
]

with open('AoC_2020_2_input.txt', 'r') as input_file:
    input_list = []
    for line in input_file:
        input_list.append(re.split('-|:|\s', line.strip()))  # split the password from the rules
    
    dict_list = []
    for line in input_list:
        this_line = {}
        this_line['min'] = int(line[0])
        this_line['max'] = int(line[1])
        this_line['char'] = line[2]
        this_line['password'] = line[4]
        dict_list.append(this_line)

    
    def check_pw(pw):
        n = pw['password'].count(pw['char'])
        if pw['min'] <= n <= pw['max']:
            return True
        return False

    print(dict_list[2]['password'].count('t'))


    valid = 0
    for line in dict_list:
        if check_pw(line):
            valid += 1
    print(valid)
