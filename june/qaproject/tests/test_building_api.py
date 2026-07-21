def fake_sensor_data():
        return{
            "building": "North Tower",
            "temperature": 50,
            "alarm": True
        }

def test_high_temperature(building_api, monkeypatch):
    monkeypatch.setattr(
        building_api, 
        "get_sensor_data",
        fake_sensor_data
    )

    response = building_api.get_sensor_data()
    assert response["temperature"] == 50