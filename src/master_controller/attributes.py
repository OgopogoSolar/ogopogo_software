import random
import time
from common.functions import number_generator
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
            self.outside_temp = outside_temp  # Outside temperature in °C
            self.inside_temp = inside_temp  # Inside temperature in °C
            self.wind_speed = wind_speed  # Wind speed in km/h
            self.wind_direction = wind_direction  # Wind direction as a compass point
            self.weather = weather  # Current weather conditions

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
        self.telemetry_history = pd.DataFrame(columns=[
            'timestamp',
            'battery_temp',
            'battery_level',
            'outside_temp',
            'inside_temp',
            'wind_speed',
            'wind_direction',
            'weather',
            'input_power',
            'output_power',
            'motor_temp',
            'brake_temp'
        ])

    # TODO: Add a method to log telemetry data to the DataFrame
    def log_data(self):
        """Logs current telemetry data to the DataFrame."""
        current_data = {
            'timestamp': datetime.now(),
            'battery_temp': self.battery_status.battery_temp,
            'battery_level': self.battery_status.battery_level,
            'outside_temp': self.environmental_data.outside_temp,
            'inside_temp': self.environmental_data.inside_temp,
            'wind_speed': self.environmental_data.wind_speed,
            'wind_direction': self.environmental_data.wind_direction,
            'weather': self.environmental_data.weather,
            'motor_temp': self.motor_temp,
            'brake_temp': self.brake_temp,
            'input_power': self.power_data.input_power,
            'output_power': self.power_data.output_power
        }
        
        # Create a new DataFrame with the current data and concatenate
        new_row = pd.DataFrame([current_data])
        self.telemetry_history = pd.concat([self.telemetry_history, new_row], ignore_index=True)

    # TODO: Add a method to save telemetry history to a CSV file
    def save_to_csv(self, filename="telemetry_data.csv"):
        """Saves telemetry history to a CSV file."""
        try:
            self.telemetry_history.to_csv(filename, index=False)
            print(f"Telemetry data saved to {filename}")
        except Exception as e:
            print(f"Error saving telemetry data: {str(e)}")

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
            telemetry_data.environmental_data.wind_direction = random.choice(["N", "S", "E", "W"])
            telemetry_data.environmental_data.weather = random.choice(["Clear", "Rainy", "Cloudy", "Stormy"])
            telemetry_data.power_data.input_power = number_generator(1, 0, 10)[0]
            telemetry_data.power_data.output_power = number_generator(1, 0, 10)[0]
            telemetry_data.motor_temp = number_generator(1, 0, 100)[0]
            telemetry_data.brake_temp = number_generator(1, 0, 100)[0]

            # TODO: Call the log_data method here to log the telemetry data
            telemetry_data.log_data()

            # Clear and display the updated data
            print("\033c", end="")
            print("Live Telemetry Data:")
            print(telemetry_data)

            # TODO: Optionally display the last few rows of telemetry history for testing
            print("\nRecent Records:")
            if len(telemetry_data.telemetry_history) > 0:
                pd.set_option('display.max_columns', None)
                pd.set_option('display.expand_frame_repr', False)
                print(telemetry_data.telemetry_history.tail().to_string())

            time.sleep(0.2)  # Refresh every 0.2 seconds
            
    except KeyboardInterrupt:
        # TODO: Save the telemetry history to a CSV file on exit
        telemetry_data.save_to_csv()
        print("\nTelemetry updates stopped.")