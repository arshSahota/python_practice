def test_building_response():
    response = {
    "building": "",
    "temperature": 28,
    "alarm": False,
    "energy_usage": 1200
}
    
    assert response["building"] != "", f"Building Name is empty"
    assert response["temperature"] <= 30, f"The temperature is not valid"
    assert response["alarm"] == False, f"The alarm should be True"
    assert response["energy_usage"] >= 0, f"The energy usage can't be negative"

#challenge 2
def test_building_response():
    response = {
    "building": "North Towers",
    "temperature": 28,
    "alarm": False,
    "energy_usage": -500
}
    
    assert response["building"] != "", f"Building Name is empty"
    assert response["temperature"] <= 30, f"The temperature is not valid"
    assert response["alarm"] == False, f"The alarm should be True"
    assert response["energy_usage"] >= 0, f"The energy usage can't be negative"