import sys
from functions import *

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

            def __str__(self):
                return f"Battery Temp: {self.battery_temp}°C, Battery Level: {self.battery_level}%"


            
            
            
    class EnvironmentalData:
        """Stores environmental telemetry data."""
        def __init__(self, outside_temp:float, inside_temp:float, wind_speed:float, wind_direction:str, weather:str):
            self.outside_temp = outside_temp  # Outside temperature in °C
            self.inside_temp = inside_temp  # Inside temperature in °C
            self.wind_speed = wind_speed  # Wind speed in km/h
            self.wind_direction = wind_direction  # Wind direction as a cardinal direction
            self.weather = weather  # Weather description (e.g., "Clear", "Rainy")
        def __str__(self):
            return (f"Outside Temp: {self.outside_temp}°C, Inside Temp: {self.inside_temp}°C, "
                    f"Wind Speed: {self.wind_speed} km/h, Wind Direction: {self.wind_direction}, "
                    f"Weather: {self.weather}")
            

    class PowerData:
        """Stores power-related telemetry data."""
        def __init__(self, input_power:float, output_power:float):
            self.input_power = input_power  # Input power from solar panels in kW
            self.output_power = output_power  # Output power consumption in kW

        def __str__(self):
            return f"Input Power: {self.input_power} kW, Output Power: {self.output_power} kW"

    def __init__(self,):
        """Initializes all telemetry data with default values."""
        self.battery_status = self.BatteryStatus(1,1)
        self.environmental_data = self.EnvironmentalData(1,1,1,"Wind_Dir","Weather")
        self.motor_temp = 60.0  # Motor temperature in °C
        self.brake_temp = 30.0  # Brake temperature in °C
        self.power_data = self.PowerData(1,1)
    
    def __str__(self):
        return (f"Battery Status: {self.battery_status}\n"
                f"Environmental Data: {self.environmental_data}\n"
                f"Motor Temp: {self.motor_temp}°C\n"
                f"Brake Temp: {self.brake_temp}°C\n"
                f"Power Data: {self.power_data}")


    def __update_data__(self,battery_temp: float, battery_level: float,
                 outside_temp: float, inside_temp: float, wind_speed: float,
                 wind_direction: str, weather: str, input_power: float,
                 output_power: float, motor_temp: float, brake_temp: float):
        """updates data"""
        
        self.battery_status.battery_temp = battery_temp
        self.battery_status.battery_level = battery_level
        self.environmental_data.outside_temp = outside_temp
        self.environmental_data.inside_temp = inside_temp
        self.environmental_data.wind_speed = wind_speed
        self.environmental_data.wind_direction = wind_direction
        self.environmental_data.weather = weather
        self.power_data.input_power = input_power
        self.power_data.output_power = output_power
        self.motor_temp =  motor_temp  # Motor temperature in °C
        self.brake_temp = brake_temp  # Brake temperature in °C
    
    # def number_generator(self, low: int, high: int):
    #     """Generates a random number between low and high."""
    #     return random.randint(low, high)
    
    def update_random_data(self):
        """Updates random data using number_generator."""
        self.__update_data__(
            self.number_generator(0, 100),  # battery_temp
            self.number_generator(0, 100),  # battery_level
            self.number_generator(0, 100),  # outside_temp
            self.number_generator(0, 100),  # inside_temp
            self.number_generator(0, 100),  # wind_speed
            "North",  # wind_direction (example)
            "Clear",  # weather (example)
            self.number_generator(0, 100),  # input_power
            self.number_generator(0, 100),  # output_power
            self.number_generator(0, 100),  # motor_temp
            self.number_generator(0, 100)   # brake_temp
        )
#Testing calling class?    
TestPowerdata = Data_Basic.PowerData(1.0,2.1)

print(TestPowerdata)
print(TestPowerdata.input_power)
print(TestPowerdata.output_power)
data_basic_class = Data_Basic()


print(data_basic_class)
data_basic_class.__update_data__(2,2,2,2,2,"Northidk","Windy",2,2,2,2)
print(data_basic_class)

data_basic_class.update_random_data()

print(data_basic_class)
