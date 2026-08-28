import pytest

def validate_temperature(temp):
    if 0 <= temp <= 50:
        return "VALID"
    elif temp > 50:
        return "TOO_HIGH"
    else:
        return "TOO_LOW"

@pytest.mark.parametrize(
    ("temp, expected"),
    [
        (-5, "TOO_LOW"),
        (0, "VALID"),
        (22, "VALID"),
        (50, "VALID"),
        (60, "TOO_HIGH")
    ]
)
def test_temps(temp, expected):
    assert validate_temperature(temp) == expected