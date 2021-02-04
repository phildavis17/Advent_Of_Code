import string

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

INPUT_PATH = Path(__file__).parent/"AoC_2020_4_input.txt"

with open(INPUT_PATH, 'r') as in_file:
    input_string = ""
    for line in in_file:
        input_string += line
    

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


def check_passport_fields(passport):
    for field in PASSPORT_FIELDS:
        if field not in passport:
            if field == "cid":
                break
            return False
    return True


#########   VALIDATION   #########


def validate_byr(byr):  #! using variables makes it easier to edit, but is it now harder to read??????
    length = 4
    min = 1920
    max = 2002
    try:  # try/except seemed like a more concise option than checking agaisnt string.digits, since we need an actual int here
        birth_year = int(byr)
    except:
        return False
    if len(byr) == length and min <= birth_year <= max:
        return True
    return False


def validate_iyr(iyr):
    length = 4
    min = 2010
    max = 2020
    try:
        issue_year = int(iyr)
    except:
        return False
    if len(iyr) == length and min <= issue_year <= max:
        return True
    return False


def validate_eyr(eyr):
    length = 4
    min = 2020
    max = 2030
    try:
        exp_year = int(eyr)
    except:
        return False
    if len(eyr) == length and min <= exp_year <= max:
        return True
    return False


def validate_hgt(hgt):  # I'm happy with this one.
    valid = {
        "in" : range(59, 77),
        "cm" : range(150, 194),
    }
    try:
        unit = hgt[-2:]
        value = int(hgt[:-2])
    except:
        return False
    if unit in valid and value in valid[unit]:
        return True
    return False


def validate_hcl(hcl):
    length = 7
    if len(hcl) == length and hcl[0] == "#":
        for c in hcl[1:]:
            if c not in string.hexdigits:
                return False
        return True
    else:
        return False


def validate_ecl(ecl):
    valid = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    if ecl in valid:
        return True
    return False


def validate_pid(pid):
    length = 9
    if len(pid) == length:
        for c in pid:
            if c not in string.digits:
                return False
        return True
    else:
        return False    


def validate_cid(*args):  # is *args a good way to handle an argument that may or may not exist?
    return True


def validate_dispatch(field, data):  # This is cool, huh?
    validator = {
        "byr" : validate_byr,
        "iyr" : validate_iyr,
        "eyr" : validate_eyr,
        "hgt" : validate_hgt,
        "hcl" : validate_hcl,
        "ecl" : validate_ecl,
        "pid" : validate_pid,
        "cid" : validate_cid,
    }
    return validator[field](data)


def validate_passport(passport):
    for field, data in passport.items():
        if not validate_dispatch(field, data):
            return False
    return True


def count_valid_passports(passports_input):
    passports = parse_input(passports_input)
    print(len(passports))
    valid = 0
    for i, passport in enumerate(passports):
        #print(passport)
        if check_passport_fields(passport):
            valid += validate_passport(passport)
    return valid


def main():
    #passports = parse_input(input_string)
    #valid_count = 0
    #for pp in passports:
    #    if check_passport_fields(pp):
    #        valid_count += 1
    #print(valid_count)

    print(count_valid_passports(input_string))


if __name__ == "__main__":
    main()