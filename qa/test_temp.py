from temp import classify_temp
from temp import check_alarm

def test_temperature_below_minimum():
    temp = 12
    expected = "LOW_TEMP"
    actual = classify_temp(temp)

    assert actual == expected, (
        f"Expected {expected} for temperature {temp}, but got {actual}"
    )


def test_temperature_at_minimum_boundary():
    temp = 18
    expected = "VALID"
    actual = classify_temp(temp)

    assert actual == expected, (
        f"Expected {expected} for temperature {temp}, but got {actual}"
    )

def test_temperature_normal_valid():
    temp = 22
    expected = "VALID"
    actual = classify_temp(temp)

    assert actual == expected, (
        f"Expected {expected} for temperature {temp}, but got {actual}"
    )

def test_temperature_at_maximum_boundary():
    temp = 30
    expected = "VALID"
    actual = classify_temp(temp)

    assert actual == expected, (
        f"Expected {expected} for temperature {temp}, but got {actual}"
    )

def test_temperature_above_maximum():
    temp = 35
    expected = "HIGH_TEMP"
    actual = classify_temp(temp)

    assert actual == expected, (
        f"Expected {expected} for temperature {temp}, but got {actual}"
    )

#mini exercise 3
# def test_temperature_above_maximum():
#     assert classify_temperature(31) == "HIGH_TEMP"

#i think I have already done it above! 

#mini exercise 4 test

def test_check_alarm():
    temp = {
        "temperature": 30
    }
    expected = False
    actual = check_alarm(temp)
    assert actual == expected, (
        f"Expected {expected} for temperature {temp} but got {actual}"
    )