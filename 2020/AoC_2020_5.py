from pathlib import Path

TRANSLATOR = {
    "F" : "0",
    "B" : "1",
    "L" : "0",
    "R" : "1",
}

INPUT_PATH = Path(__file__).parent/"AoC_2020_5_input.txt"

with open(INPUT_PATH, 'r') as in_file:
    seat_codes = []
    for line in in_file:
        seat_codes.append(line.strip())


def parse_seat_code(seat_code):
    row = "0b"
    col = "0b"    
    for c in seat_code[:-3]:
        row += TRANSLATOR[c.upper()]
    row = int(row, 2)
    for c in seat_code[-3:]:
        col += TRANSLATOR[c.upper()]
    col = int(col, 2)
    id = row * 8 + col

    seat = {}
    seat["row"] = row
    seat["col"]= col
    seat["ID"] = id

    return seat


def main():
    max = 0
    seat_IDs = set()
    missing_nos = []

    for seat_code in seat_codes:
        id = parse_seat_code(seat_code)["ID"]
        seat_IDs.add(id)
        if id > max:
            max = id
    
    for i in range(max+1):
        if i not in seat_IDs:
            missing_nos.append(i)

    print(missing_nos)


if __name__ == "__main__":
    main()