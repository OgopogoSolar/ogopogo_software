import time  # For potential delay in loops
import logging  # For logging alerts (optional)

# Configure logging
logging.basicConfig(
    filename='alert_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AlertSystem:
    """
    A basic skeleton for an alert system to monitor telemetry data and trigger alerts.
    """
    def __init__(self):
        """Initialize thresholds and a structure to hold active alerts."""
        # Define thresholds for different parameters
        self.thresholds = {
            "battery_temp_high": 60.0,  # Temperature in Celsius
            "battery_level_low": 20.0,  # Percentage
            "motor_temp_high": 80.0     # Temperature in Celsius
        }
        # Initialize empty list to store active alerts
        self.active_alerts = []
        logger.info("AlertSystem initialized with standard thresholds")


        # Check telemetry data against thresholds and trigger alerts if needed.
        # Args: telemetry_data: Dictionary containing current telemetry values
        # Returns: List of new alert messages that were triggered
    def check_alerts(self, telemetry_data):
        """
        Check telemetry data against thresholds and add triggered alerts.
        :param telemetry_data: An instance of the Attributes class containing telemetry data.
        """
        try:
            # Check battery temperature
            if "battery_temp" in telemetry_data:
                if telemetry_data["battery_temp"] > self.thresholds["battery_temp_high"]:
                    alert_msg = f"WARNING: Battery temperature ({telemetry_data['battery_temp']}°C) exceeds threshold ({self.thresholds['battery_temp_high']}°C)"
                    if alert_msg not in self.active_alerts:
                        self.active_alerts.append(alert_msg)
                        logger.warning(alert_msg)

            # Check battery level
            if "battery_level" in telemetry_data:
                if telemetry_data["battery_level"] < self.thresholds["battery_level_low"]:
                    alert_msg = f"WARNING: Low battery level ({telemetry_data['battery_level']}%) below threshold ({self.thresholds['battery_level_low']}%)"
                    if alert_msg not in self.active_alerts:
                        self.active_alerts.append(alert_msg)
                        logger.warning(alert_msg)

            # Check motor temperature
            if "motor_temp" in telemetry_data:
                if telemetry_data["motor_temp"] > self.thresholds["motor_temp_high"]:
                    alert_msg = f"WARNING: Motor temperature ({telemetry_data['motor_temp']}°C) exceeds threshold ({self.thresholds['motor_temp_high']}°C)"
                    if alert_msg not in self.active_alerts:
                        self.active_alerts.append(alert_msg)
                        logger.warning(alert_msg)

        except Exception as e:
            logger.error(f"Error checking alerts: {str(e)}")
            raise


        # Display all active alerts
    def display_alerts(self):
        """
        Display active alerts in a readable format.
        """
        if not self.active_alerts:
            print("No active alerts.")
            logger.info("Displayed alerts: none active")
            return

        print("\n=== ACTIVE ALERTS ===")
        for i, alert in enumerate(self.active_alerts, 1):
            print(f"{i}. {alert}")
        print("===================\n")
        logger.info(f"Displayed {len(self.active_alerts)} active alerts")



        # Clear all active alerts.
        # Returns: Number of alerts that were cleared
    def clear_alerts(self):
        """
        Clear the list of active alerts.
        """
        num_cleared = len(self.active_alerts)
        self.active_alerts.clear()
        logger.info(f"Cleared {num_cleared} alerts")

# For testing purposes
if __name__ == "__main__":
    # from attributes import Attributes  # Uncomment when Attributes is implemented
    alert_system = AlertSystem()
    
    # Simulated telemetry data for testing
    test_data = {
        "battery_temp": 55.0,
        "battery_level": 75.0,
        "motor_temp": 65.0
    }
    
    try:
        while True:
            # Simulate changing temperature
            test_data["battery_temp"] += 2  # Simulate increasing temperature
            test_data["battery_level"] -= 1  # Simulate decreasing battery
            test_data["motor_temp"] += 3  # Simulate increasing motor temperature
            
            # Check for alerts
            alert_system.check_alerts(test_data)
            
            # Display alerts
            print("\033c", end="")  # Clear console for better readability
            print("Telemetry Alerts:")
            print(f"Current Readings:")
            print(f"Battery Temperature: {test_data['battery_temp']}°C")
            print(f"Battery Level: {test_data['battery_level']}%")
            print(f"Motor Temperature: {test_data['motor_temp']}°C")
            print("\nAlerts:")
            alert_system.display_alerts()
            
            #Add delay for readability
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nAlert system test interrupted.")