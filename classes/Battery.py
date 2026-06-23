class Battery:
    def __init__(self, charge_level):
        self.charge_level = charge_level

class Phone:
    def __init__(self):
        self.battery = Battery()


    def show_battery(self):
        return self.battery.charge_level 
    
battery = Battery()