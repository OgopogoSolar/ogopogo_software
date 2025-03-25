import sys
import struct
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, 
                             QTextEdit, QComboBox, QLabel)
from PyQt6.QtCore import QThread, pyqtSignal
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class SerialReader(QThread):
    data_received = pyqtSignal(list)
    
    def __init__(self, port, baud_rate=312500, timeout=3):
        super().__init__()
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.running = True
        self.ser = None  # Initialize to None to prevent attribute errors

    def run(self):
        try:
            self.ser = serial.Serial(self.port, self.baud_rate, timeout=self.timeout)
            while self.running:
                if self.ser.in_waiting >= 16:  # 4 floats * 4 bytes = 16 bytes
                    raw_data = self.ser.read(16)
                    try:
                        floats = struct.unpack('<4f', raw_data)
                        self.data_received.emit(list(floats))
                    except struct.error:
                        print("Data unpacking error")
        except serial.SerialException as e:
            print(f"Serial Exception: {e}")
        finally:
            if self.ser and self.ser.is_open:
                self.ser.close()
    
    def stop(self):
        self.running = False
        self.wait()

class SerialMonitorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.serial_thread = None
        self.data_series = [[], [], [], []]  # Only 4 data channels (matching 4 floats)

    def initUI(self):
        layout = QVBoxLayout()
        
        self.label = QLabel("Select Serial Port:")
        layout.addWidget(self.label)
        
        self.port_selector = QComboBox()
        self.refresh_ports()
        layout.addWidget(self.port_selector)
        
        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_serial)
        layout.addWidget(self.connect_button)
        
        self.disconnect_button = QPushButton("Disconnect")
        self.disconnect_button.setEnabled(False)
        self.disconnect_button.clicked.connect(self.disconnect_serial)
        layout.addWidget(self.disconnect_button)
        
        self.data_display = QTextEdit()
        self.data_display.setReadOnly(True)
        layout.addWidget(self.data_display)
        
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        
        self.setLayout(layout)
        self.setWindowTitle("Serial Monitor with Visualization")
        self.resize(600, 400)
    
    def refresh_ports(self):
        self.port_selector.clear()
        ports = [port.device for port in serial.tools.list_ports.comports()]
        self.port_selector.addItems(ports)
    
    def connect_serial(self):
        selected_port = self.port_selector.currentText()
        if not selected_port:
            self.data_display.append("No port selected!")
            return
        
        self.serial_thread = SerialReader(selected_port)
        self.serial_thread.data_received.connect(self.display_data)
        self.serial_thread.start()
        
        self.connect_button.setEnabled(False)
        self.disconnect_button.setEnabled(True)

        # Send command to MCU if serial is initialized
        if self.serial_thread.ser and self.serial_thread.ser.is_open:
            self.serial_thread.ser.write(b'\x01')
    
    def disconnect_serial(self):
        # Send disconnect command if serial is initialized
        if self.serial_thread and self.serial_thread.ser and self.serial_thread.ser.is_open:
            self.serial_thread.ser.write(b'\x00')
        
        if self.serial_thread:
            self.serial_thread.stop()
        
        self.connect_button.setEnabled(True)
        self.disconnect_button.setEnabled(False)
    
    def display_data(self, data):
        self.data_display.append(f"Received: {data}")

        # Ensure data is the correct length (4 floats)
        if len(data) != 4:
            return
        
        # Store the received values
        for i in range(4):
            self.data_series[i].append(data[i])

        # Limit number of points shown (max 500)
        if len(self.data_series[0]) > 500:
            for i in range(4):
                self.data_series[i].pop(0)  # Remove the oldest data point
        
        self.update_plot()
    
    def update_plot(self):
        self.ax.clear()
        for i in range(4):
            self.ax.plot(self.data_series[i], label=f"Float {i+1}")
        
        self.ax.legend()
        self.ax.set_title("Real-time Float Data")
        self.ax.set_xlabel("Sample Number")
        self.ax.set_ylabel("Value")
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialMonitorApp()
    window.show()
    sys.exit(app.exec())
