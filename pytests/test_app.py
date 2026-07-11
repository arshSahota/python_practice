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
        ([], 0),
        ([{"severity": "HIGH"}], 1),
        ([{"severity": "HIGH"}, {"severity": "HIGH"}], 2)
    ]
)

def test_count_high_alarms(alarms, expected):

    assert count_high_alarms(alarms) == expected