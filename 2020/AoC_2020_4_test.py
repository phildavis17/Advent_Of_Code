from AoC_2020_4 import *  # Wildcard seemed appropriate here. Is this good practice?

BAD_PASSPORTS = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

GOOD_PASSPORTS = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""


def test_validate_byr():
    assert validate_byr("2002") == True
    assert validate_byr("2003") == False

def test_validate_iyr():
    assert validate_iyr("2010") == True
    assert validate_iyr("2009") == False

def test_validate_eyr():
    assert validate_eyr("2030") == True
    assert validate_eyr("2020") == True
    assert validate_eyr("2025") == True
    assert validate_eyr("2031") == False

def test_validate_hgt():
    assert validate_hgt("59in") == True
    assert validate_hgt("76in") == True
    assert validate_hgt("190cm") == True
    assert validate_hgt("190in") == False
    assert validate_hgt("190") == False
    assert validate_hgt("19") == False

def test_validate_hcl():
    assert validate_hcl("#123abc") == True
    assert validate_hcl("#123abz") == False
    assert validate_hcl("123abc") == False

def test_validate_ecl():
    assert validate_ecl("brn") == True
    assert validate_ecl("wat") == False

def test_validate_pid():
    assert validate_pid("000000001") == True
    assert validate_pid("0123456789") == False

def test_count_valid_passports():
    assert count_valid_passports(BAD_PASSPORTS) == 0
    assert count_valid_passports(GOOD_PASSPORTS) == 4

