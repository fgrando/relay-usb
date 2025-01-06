#!/usr/bin/python3
import serial
import argparse

def control_device(serial_port, action):
    ser = serial.Serial(serial_port, 9600)  # Replace 'COM1' with the correct port name, and set baud rate (e.g., 9600)
    data = b'\xA0\x01\x00\xA1' # off
    if action == 'on':
        data = b'\xA0\x01\x01\xA2' # on
    ser.write(data)
    ser.close()

def main():
    parser = argparse.ArgumentParser(description="Control usb relay device.")
    parser.add_argument("serial_port", type=str, help="Path to serial port")
    parser.add_argument("action", choices=['on', 'off'], help="Action to control the device (on or off)")
    args = parser.parse_args()
    control_device(args.serial_port, args.action)

if __name__ == "__main__":
    main()
