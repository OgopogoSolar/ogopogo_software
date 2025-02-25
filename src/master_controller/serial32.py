import sys
import serial
import threading
import time
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel

ports = [
    '/dev/tty10'
]

class SerialMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.serial_thread = None
        self.running = False
        self.ser = None

    def initUI(self):
        layout = QVBoxLayout()

        self.start_button = QPushButton("Start Monitoring")
        self.start_button.clicked.connect(self.start_monitoring)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Monitoring")
        self.stop_button.clicked.connect(self.stop_monitoring)
        self.stop_button.setEnabled(False)
        layout.addWidget(self.stop_button)
        
        self.data_display = QTextEdit()
        self.data_display.setReadOnly(True)
        layout.addWidget(self.data_display)
        
        self.setLayout(layout)
        self.setWindowTitle("Serial Port Monitor")
        self.resize(400, 300)

    def start_monitoring(self):
        self.running = True
        self.serial_thread = threading.Thread(target=self.scan_ports, daemon=True)
        self.serial_thread.start()
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.data_display.append("Scanning ports...")

    def stop_monitoring(self):
        self.running = False
        if self.ser:
            self.ser.close()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.data_display.append("Stopped monitoring.")

    def scan_ports(self):
        for port in ports:
            if not self.running:
                return
            try:
                self.ser = serial.Serial(port, 312500, timeout=3)
                self.data_display.append(f"Connected to {port}")
                self.read_serial()
                self.ser.close()
            except serial.SerialException:
                continue

    def read_serial(self):
        while self.running and self.ser:
            try:
                if self.ser.in_waiting > 0:
                    data = self.ser.readline().decode('utf-8').strip()
                    try:
                        float_value = float(data)
                        self.data_display.append(f"Received float: {float_value}")
                    except ValueError:
                        self.data_display.append(f"Invalid data: {data}")
            except Exception as e:
                self.data_display.append(f"Error reading data: {e}")
            time.sleep(0.1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SerialMonitor()
    window.show()
    sys.exit(app.exec())
