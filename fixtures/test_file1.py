import pytest

@pytest.fixture
def sample_devices():
    devices = [
    {
        "device": "AHU-01",
        "status": "online",
        "alarms": 0
    },
    {
        "device": "VAV-01",
        "status": "offline",
        "alarms": 2
    }
    ]
    return devices

def test_number_devices(sample_devices):
    assert len(sample_devices) == 2

def test_first_device(sample_devices):
    assert sample_devices[0]["status"] == "online"

def test_second_device(sample_devices):
    assert sample_devices[1]["alarms"] == 2