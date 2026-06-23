class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius   # ← go through setter

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, val):
        if val < -273.15:
            raise ValueError("Cannot set this temperature")
        self._celsius = val 
