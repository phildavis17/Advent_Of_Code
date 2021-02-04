from pathlib import Path

TEST_DATA = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


PASSPORT_FIELDS = {
    "byr" : "Birth Year",
    "iyr" : "Issue Year",
    "eyr" : "Expiration Year",
    "hgt" : "Height",
    "hcl" : "Hair Color",
    "ecl" : "Eye Color",
    "pid" : "Passport ID",
    "cid" : "Country ID",
}

INPUT_PATH = Path(R"C:\Documents\Code\Advent_Of_Code\2020\AoC_2020_4_input.txt")
with open(INPUT_PATH, 'r') as in_file:
    input_string = ""
    for line in in_file:
        input_string += line
    print(len(input_string))

def parse_input(raw_input):
    # Split on double newline
    line_input = raw_input.split("\n\n")
    input_dicts = []
    for line in line_input:
        if line:
            line_dict = {}
            for field in line.split():
                k, v = field.split(":")
                line_dict[k] = v
        input_dicts.append(line_dict)    
    return input_dicts

def check_passport(passport):
    for field in PASSPORT_FIELDS:
        if field not in passport:
            if field == "cid":
                break
            return False
    return True

def main():
    passports = parse_input(input_string)
    valid_count = 0
    for pp in passports:
        if check_passport(pp):
            valid_count += 1
    print(valid_count)


if __name__ == "__main__":
    main()