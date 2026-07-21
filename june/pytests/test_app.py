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
        pytest.param(["RTU"], False, id="empty-list"),
        pytest.param(["RTU", "AHU"], False, id="one-device"),
        pytest.param(["AHU", "RTU", "RTU"], True, id = "duplicate-found")
    ]
)

def test_has_duplicates(alarms, expected):
    assert has_duplicates(alarms) == expected