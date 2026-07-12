import pytest

# def test_valid_sensor_data(valid_sensor_response):
#     response = valid_sensor_response
#     assert response["building"] != ""
#     assert response["temperature"] > 30
#     assert response["alarm"] is True
#     assert response["energy_usage"] > 0

def test_low_temp_sensor(low_temp_sensor):
    response = low_temp_sensor
    assert response["building"] != ""
    assert response["temperature"] < 18
    assert response["alarm"] is False
    assert response["energy_usage"] > 0


"""
if the response becomes
{
    "building": "South Tower",
    "temperature": 15,
    "alarm": True,
    "energy_usage": 700
}
i would first investigate
whether is is an testing issue, application issue or requirements or business rule issue
"""