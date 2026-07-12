def test_high_temperature_sensor(building_api):

    response = building_api.get_sensor_data()

    assert response["status_code"] == 200

    data = response["data"]

    assert data["temperature"] > 30
    assert data["alarm"] is True

def test_low_temperature_sensor(building_api):

    response = building_api.get_low_temp_sensor()

    assert response["status_code"] == 200

    data = response["data"]

    assert data["temperature"] < 18
    assert data["alarm"] is False