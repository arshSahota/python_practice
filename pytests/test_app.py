import pytest
from app import (
    count_critical_alarms,
    count_high_alarms,
    has_duplicates,
    find_offline_devices
)

@pytest.mark.parametrize(
    "alarms, expected",
    [
        (["RTU"], False),
        (["RTU", "AHU"], False),
        (["AHU", "RTU", "RTU"], True)
    ]
)

def test_has_duplicates(alarms, expected):
    assert has_duplicates(alarms) == expected