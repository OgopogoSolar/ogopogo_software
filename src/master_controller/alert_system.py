import time  # For potential delay in loops
import logging  # For logging alerts (optional)
from attributes import Attributes  # Uncomment when Attributes is implemented
from common.functions import number_generator  # Uncomment when necessary

class AlertSystem:
    def __init__(self):
        """Initialize thresholds and a structure to hold active alerts."""
        # Configure logging
        logging.basicConfig(
            filename='alert_system.log',
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # TODO: Define a dictionary or other data structure for thresholds.
        # Example: self.thresholds = {"battery_temp_high": 60.0, "battery_level_low": 20.0}
        self.thresholds = {
            "battery_temp_high": 60.0,  # °C
            "battery_level_low": 20.0,  # %
            "motor_temp_high": 80.0,    # °C
            "wind_speed_high": 100.0,   # km/h
            "outside_temp_high": 45.0,  # °C
            "outside_temp_low": -30.0,  # °C
            "power_imbalance": 1.0      # kW
        }
        
        self.active_alerts = []
        self.logger.info("AlertSystem initialized")

    def check_alerts(self, telemetry_data):
        """
        Check telemetry data against thresholds and add triggered alerts.
        :param telemetry_data: An instance of the Attributes class containing telemetry data.
        """
        # TODO: Compare telemetry values (e.g., battery_temp) with thresholds.
        # TODO: Append triggered alerts to a list or similar structure.
        try:
            # Battery temperature check
            if telemetry_data.battery_status.battery_temp > self.thresholds["battery_temp_high"]:
                alert_msg = f"WARNING: Battery temperature ({telemetry_data.battery_status.battery_temp:.1f}°C) exceeds threshold ({self.thresholds['battery_temp_high']}°C)"
                if alert_msg not in self.active_alerts:
                    self.active_alerts.append(alert_msg)
                    self.logger.warning(alert_msg)
            
            # Battery level check
            if telemetry_data.battery_status.battery_level < self.thresholds["battery_level_low"]:
                alert_msg = f"WARNING: Low battery level ({telemetry_data.battery_status.battery_level:.1f}%) below threshold ({self.thresholds['battery_level_low']}%)"
                if alert_msg not in self.active_alerts:
                    self.active_alerts.append(alert_msg)
                    self.logger.warning(alert_msg)
            
            # Motor temperature check
            if telemetry_data.motor_temp > self.thresholds["motor_temp_high"]:
                alert_msg = f"WARNING: Motor temperature ({telemetry_data.motor_temp:.1f}°C) exceeds threshold ({self.thresholds['motor_temp_high']}°C)"
                if alert_msg not in self.active_alerts:
                    self.active_alerts.append(alert_msg)
                    self.logger.warning(alert_msg)
            
            # Wind speed check
            if telemetry_data.environmental_data.wind_speed > self.thresholds["wind_speed_high"]:
                alert_msg = f"WARNING: High wind speed ({telemetry_data.environmental_data.wind_speed:.1f} km/h) exceeds threshold ({self.thresholds['wind_speed_high']} km/h)"
                if alert_msg not in self.active_alerts:
                    self.active_alerts.append(alert_msg)
                    self.logger.warning(alert_msg)
            
            # Outside temperature checks
            if telemetry_data.environmental_data.outside_temp > self.thresholds["outside_temp_high"]:
                alert_msg = f"WARNING: High outside temperature ({telemetry_data.environmental_data.outside_temp:.1f}°C) exceeds threshold ({self.thresholds['outside_temp_high']}°C)"
                if alert_msg not in self.active_alerts:
                    self.active_alerts.append(alert_msg)
                    self.logger.warning(alert_msg)
            elif telemetry_data.environmental_data.outside_temp < self.thresholds["outside_temp_low"]:
                alert_msg = f"WARNING: Low outside temperature ({telemetry_data.environmental_data.outside_temp:.1f}°C) below threshold ({self.thresholds['outside_temp_low']}°C)"
                if alert_msg not in self.active_alerts:
                    self.active_alerts.append(alert_msg)
                    self.logger.warning(alert_msg)
            
            # Power imbalance check
            power_diff = abs(telemetry_data.power_data.input_power - telemetry_data.power_data.output_power)
            if power_diff > self.thresholds["power_imbalance"]:
                alert_msg = f"WARNING: Power imbalance detected ({power_diff:.1f} kW) exceeds threshold ({self.thresholds['power_imbalance']} kW)"
                if alert_msg not in self.active_alerts:
                    self.active_alerts.append(alert_msg)
                    self.logger.warning(alert_msg)

        except Exception as e:
            self.logger.error(f"Error checking alerts: {str(e)}")
            raise

    def display_alerts(self):
        """Display active alerts in a readable format."""
        # TODO: Print active alerts to the console or another output medium.
        if not self.active_alerts:
            print("No active alerts")
            self.logger.info("No alerts to display")
            return
        
        print("\nActive Alerts:")
        print("==============")
        for i, alert in enumerate(self.active_alerts, 1):
            print(f"{i}. {alert}")
        print("==============\n")
        self.logger.info(f"Displayed {len(self.active_alerts)} active alerts")

    def clear_alerts(self):
        """Clear the list of active alerts."""
        # TODO: Reset the list of active alerts.
        num_cleared = len(self.active_alerts)
        self.active_alerts.clear()
        self.logger.info(f"Cleared {num_cleared} alerts")
        return num_cleared

if __name__ == "__main__":
    # TODO: Create an instance of Attributes when available
    telemetry_data = Attributes()  # Replace with an instance of Attributes when available

    alert_system = AlertSystem()

    try:
        while True:
            # TODO: Generate or fetch telemetry data (simulate or integrate Attributes class).
            # telemetry_data.<property> = <random value>
            telemetry_data.battery_status.battery_temp = number_generator(1, 0, 100)[0]
            telemetry_data.battery_status.battery_level = number_generator(1, 0, 100)[0]
            telemetry_data.environmental_data.outside_temp = number_generator(1, -40, 50)[0]
            telemetry_data.environmental_data.inside_temp = number_generator(1, 15, 30)[0]
            telemetry_data.environmental_data.wind_speed = number_generator(1, 0, 150)[0]
            telemetry_data.power_data.input_power = number_generator(1, 0, 10)[0]
            telemetry_data.power_data.output_power = number_generator(1, 0, 10)[0]
            telemetry_data.motor_temp = number_generator(1, 0, 100)[0]
            telemetry_data.brake_temp = number_generator(1, 0, 100)[0]

            # TODO: Use the alert system to check telemetry data.
            alert_system.check_alerts(telemetry_data)

            # Clear console and display current state
            print("\033c", end="")
            print("Telemetry Data:")
            print(telemetry_data)
            alert_system.display_alerts()

            # TODO: Add delay or loop control as needed (e.g., time.sleep).
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nAlert system test interrupted.")