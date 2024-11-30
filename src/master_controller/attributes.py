import random
import time
from common.functions import *
import pandas as pd
from datetime import datetime

class Attributes:
    '''
    A basic Python class that stores telemetry data and allows external updates for testing.
    '''

    class BatteryStatus:
        """Stores battery-related telemetry data."""
        def __init__(self, battery_temp: float = 0.0, battery_level: float = 0.0):
            self.battery_temp = battery_temp  # Battery temperature in °C
            self.battery_level = battery_level  # Battery level as a percentage

        def __str__(self):
            return f"Battery Temp: {self.battery_temp:.2f}°C, Battery Level: {self.battery_level:.2f}%"

    class EnvironmentalData:
        """Stores environmental telemetry data."""
        def __init__(self, outside_temp: float = 0.0, inside_temp: float = 0.0,
                     wind_speed: float = 0.0, wind_direction: str = "N/A", weather: str = "N/A"):
            self.outside_temp = outside_temp # Outside temperature in °C
            self.inside_temp = inside_temp # Inside temperature in °C
            self.wind_speed = wind_speed # Wind speed in km/h
            self.wind_direction = wind_direction # Wind direction as a compass point
            self.weather = weather # Current weather conditions (N, S, E, W)

        def __str__(self):
            return (f"Outside Temp: {self.outside_temp:.2f}°C, Inside Temp: {self.inside_temp:.2f}°C, "
                    f"Wind Speed: {self.wind_speed:.2f} km/h, Wind Direction: {self.wind_direction}, "
                    f"Weather: {self.weather}")

    class PowerData:
        """Stores power-related telemetry data."""
        def __init__(self, input_power: float = 0.0, output_power: float = 0.0):
            self.input_power = input_power  # Input power from solar panels in kW
            self.output_power = output_power  # Output power consumption in kW

        def __str__(self):
            return f"Input Power: {self.input_power:.2f} kW, Output Power: {self.output_power:.2f} kW"

    def __init__(self):
        """Initializes all telemetry data with default values."""
        self.battery_status = self.BatteryStatus()
        self.environmental_data = self.EnvironmentalData()
        self.motor_temp = 60.0  # Motor temperature in °C
        self.brake_temp = 30.0  # Brake temperature in °C
        self.power_data = self.PowerData()

        # TODO: Add a pandas DataFrame for telemetry history
        pass

    # TODO: Add a method to log telemetry data to the DataFrame
    def log_data(self):
        """Logs current telemetry data to the DataFrame."""
        pass

    # TODO: Add a method to save telemetry history to a CSV file
    def save_to_csv(self, filename="telemetry_data.csv"):
        """Saves telemetry history to a CSV file."""
        pass

    def __str__(self):
        return (f"{self.battery_status}\n"
                f"{self.environmental_data}\n"
                f"Motor Temp: {self.motor_temp:.2f}°C, Brake Temp: {self.brake_temp:.2f}°C\n"
                f"{self.power_data}")
    
# Main function for testing
if __name__ == "__main__":
    telemetry_data = Attributes()

    try:
        while True:
            # Generate random test data directly for each component
            telemetry_data.battery_status.battery_temp = number_generator(1, 0, 100)[0]
            telemetry_data.battery_status.battery_level = number_generator(1, 0, 100)[0]
            telemetry_data.environmental_data.outside_temp = number_generator(1, -40, 50)[0]
            telemetry_data.environmental_data.inside_temp = number_generator(1, 15, 30)[0]
            telemetry_data.environmental_data.wind_speed = number_generator(1, 0, 150)[0]
            telemetry_data.environmental_data.wind_direction = random.choice(["North", "South", "East", "West"])
            telemetry_data.environmental_data.weather = random.choice(["Clear", "Rainy", "Cloudy", "Stormy"])
            telemetry_data.power_data.input_power = number_generator(1, 0, 10)[0]
            telemetry_data.power_data.output_power = number_generator(1, 0, 10)[0]
            telemetry_data.motor_temp = number_generator(1, 0, 100)[0]
            telemetry_data.brake_temp = number_generator(1, 0, 100)[0]

            # TODO: Call the log_data method here to log the telemetry data
            # add code to call the log_data method

            # Clear and display the updated data
            print("\033c", end="")
            print("Live Telemetry Data:")
            print(telemetry_data)

            # TODO: Optionally display the last few rows of telemetry history for testing
            # add code to display the last few rows of the DataFrame

            time.sleep(0.2)  # Refresh every 0.2 seconds
    except KeyboardInterrupt:
        # TODO: Save the telemetry history to a CSV file on exit
        # add code to save the telemetry history to a CSV file

        print("Telemetry updates stopped.")
