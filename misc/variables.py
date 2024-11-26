
class Data_Basic:
    '''
    A basic python class that stores telemetry data

    This version uses basic data types instead of linkedlists,arrays,etc 
    (unsure of what data structures i should use)

    '''

    class BatteryStatus:
        """Stores battery-related telemetry data."""
        def __init__(self, battery_temp:float, battery_level:float):
            self.battery_temp = battery_temp  # Battery temperature in °C
            self.battery_level = battery_level  # Battery level as a percentage

            #Getters/setters template? not sure if i need them in python idk what im doing
            def set_battery_temp(self,battery:float):
                self.battery_temp = battery
                
            def get_battery_temp(self):
                return battery_temp
            
            
    class EnvironmentalData:
        """Stores environmental telemetry data."""
        def __init__(self, outside_temp:float, inside_temp:float, wind_speed:float, wind_direction:str, weather:str):
            self.outside_temp = outside_temp  # Outside temperature in °C
            self.inside_temp = inside_temp  # Inside temperature in °C
            self.wind_speed = wind_speed  # Wind speed in km/h
            self.wind_direction = wind_direction  # Wind direction as a cardinal direction
            self.weather = weather  # Weather description (e.g., "Clear", "Rainy")

            

    class PowerData:
        """Stores power-related telemetry data."""
        def __init__(self, input_power:float, output_power:float):
            self.input_power = input_power  # Input power from solar panels in kW
            self.output_power = output_power  # Output power consumption in kW

    def __init__(self):
        """Initializes all telemetry data with default values."""
        self.battery_status = self.BatteryStatus()
        self.environmental_data = self.EnvironmentalData()
        self.motor_temp = 60.0  # Motor temperature in °C
        self.brake_temp = 30.0  # Brake temperature in °C
        self.power_data = self.PowerData()


#Testing calling class?    
TestPowerdata = Data_Basic.PowerData(1.0,2.1)

print(TestPowerdata)
print(TestPowerdata.input_power)
print(TestPowerdata.output_power)

        



