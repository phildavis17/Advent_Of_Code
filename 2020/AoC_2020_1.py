# Find the two entries that sum to 2020 and then multiply those two numbers together.

import itertools

TEST_INPUT = [
    1721,
    979,
    366,
    299,
    675,
    1456
]


def check_sum(numbers, target):
    for i, num in enumerate(numbers):
        for i2, num2 in enumerate(numbers):
            if i == i2: continue
            if num + num2 == target:
                return (i, i2)



def problem_1():
    with open("AoC_2020_1_input.txt", 'r') as input_file:
        input_list = []
        for line in input_file:
            #print(line)
            input_list.append(int(line))
        #print(len(input_list))
        a, b = check_sum(input_list, 2020)
        result = input_list[a] * input_list[b]
        print(result)


def main():
    with open("AoC_2020_1_inputs.txt", 'r') as input_file:
        input_list = [int(line) for line in input_file]
        
        index_list = range(len(input_list))
        for combo in itertools.combinations(index_list, 3):
            sum = 0
            prod = 1
            for i in combo:
                sum += input_list[i]
                prod *= input_list[i]
            if sum == 2020:
                print(prod)
        

if __name__ == "__main__":
    main()

