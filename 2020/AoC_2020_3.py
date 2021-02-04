from pathlib import Path

in_file = Path(R"AoC_2020_3_input.txt")

input_list = []
with open(in_file, 'r') as input_file:
    for line in input_file:
        input_list.append(line.strip())


START_POS = (1, 1)
SLOPE = (3, 1)
SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

def generate_slope_points(field, start_pos ,slope):
    point_list = [start_pos]
    (x, y) = start_pos
    (step_x, step_y) = slope
    wrap = len(field[0])
    
    while point_list[-1][1] < len(field):
        (x, y) = point_list[-1]
        next_x = (x + step_x) % wrap
        next_y = y + step_y
        point_list.append((next_x, next_y))
        x, y = next_x, next_y
    
    return(point_list)




def check_slope(field, point_list):
    '''Looks at spots on a given slope and checks them for a target character'''
    CHECK_CHAR = '#'
    trees = 0
    for point in point_list:
        (x, y) = point
        x, y = x - 1, y - 1
        #print(field[y][x])
        if field[y][x] == CHECK_CHAR:
            trees += 1

    return trees





if __name__ == "__main__":
    tree_totals = []
    for s in SLOPES:
        p_list = generate_slope_points(input_list, START_POS, s)
        tree_totals.append(check_slope(input_list, p_list))
    ans = 1
    for t in tree_totals:
        ans *= t
    print(tree_totals)
    print(ans)
