class BuildingAPI:

    def get_sensor_data(self):
        return {
            "status_code": 200,
            "data": {
                "building": "North Tower",
                "temperature": 35,
                "alarm": True,
                "energy_usage": 1200
            }
        }

    def get_low_temp_sensor(self):
        return {
            "status_code": 200,
            "data": {
                "building": "South Tower",
                "temperature": 15,
                "alarm": False,
                "energy_usage": 700
            }
        }