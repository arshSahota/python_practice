import pytest

response = {
    "status_code": 200,
    "data": {
        "sensor_id": "S001",
        "temperature": 110,
        "alarm": True
    }
}

def test_response():
    data = response["data"]

    assert "temperature" in data

    if data["temperature"] > 100:
        assert data["alarm"] is True