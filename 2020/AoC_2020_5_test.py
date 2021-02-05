from AoC_2020_5 import *

def test_parse_seat_code():
    seat = parse_seat_code("FBFBBFFRLR")
    assert seat["row"] == 44
    assert seat["col"] == 5
    assert seat["ID"] == 357