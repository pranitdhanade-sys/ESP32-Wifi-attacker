import os
import sys
import subprocess
import serial.tools.list_ports


# =============================
# PORT DETECTION
# =============================

def find_esp32_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if any(keyword in port.description for keyword in ["USB Serial Device", "CP210", "CH340"]):
            return port.device
    return None


# =============================
# SKETCH UPLOAD
# =============================

def upload_sketch(sketch_name):
    base_path = "/home/violet/Documents/Flipper0/sketch"
    sketch_path = os.path.join(base_path, sketch_name)

    board = "esp32:esp32:esp32dev"
    esp32_port = find_esp32_port()

    if not esp32_port:
        print("ESP32 not detected.")
        return

    try:
        subprocess.run(
            ["arduino-cli", "upload", "-p", esp32_port, "--fqbn", board, sketch_path],
            check=True
        )
        print("Upload successful!")
    except subprocess.CalledProcessError:
        print("Upload failed.")


# =============================
# UTIL
# =============================

def clear():
    os.system("clear")


def pause():
    input("\nPress Enter to continue...")


# =============================
# WIFI MENU
# =============================

def wifi_menu():
    sketch_map = {
        "1": "hidden_ssid.ino",
        "2": "rssi_monitor.ino",
        "3": "channel_util.ino",
        "4": "packet_rate.ino",
        "5": "mac_randomizer.ino",
        "6": "beacon_analyzer.ino",
        "7": "wifi_logger.ino",
        "8": "client_counter.ino",
        "9": "rogue_ap_detector.ino"
    }

    while True:
        clear()
        print("""
======== WiFi Research ========

[1] Hidden SSID Detector
[2] RSSI Monitor
[3] Channel Utilization Monitor
[4] Packet Rate Analyzer
[5] MAC Randomization Tool
[6] Beacon Frame Analyzer
[7] WiFi Signal Logger (CSV)
[8] Client Counter
[9] Rogue AP Detector (Defensive)
[0] Back
""")

        choice = input("Select: ")

        if choice == "0":
            return

        if choice in sketch_map:
            upload_sketch(sketch_map[choice])
        else:
            print("Invalid Option")

        pause()


# =============================
# BLE Research
# =============================

def ble_menu():
    ble_sketch_map = {
    "1": "ble_scanner.ino",
    "2": "ble_adv_logger.ino",
    "3": "ble_service_enum.ino",
    "4": "ble_rssi_tracker.ino",
    "5": "ble_uuid_filter.ino",
    "6": "ble_battery_monitor.ino",
    "7": "ble_device_classifier.ino",
    "8": "ble_connection_logger.ino",
    "9": "ble_gatt_explorer.ino"
}

    while True:
        clear()
        print("""
======== BLE Research ========

[1] BLE Device Scanner
[2] BLE Advertisement Logger
[3] BLE Service Enumerator
[4] BLE Signal Strength Tracker
[5] BLE UUID Filter
[6] BLE Battery Service Monitor
[7] BLE Device Classifier
[8] BLE Connection Logger
[9] BLE GATT Explorer
[0] Back
""")
	choice = input("Select: ")

	if choice == "0":
    		return

	if choice in ble_sketch_map:
    	    upload_sketch(ble_sketch_map[choice])
	else:
            print("Invalid Option")



# =============================
# RFID / NFC Research
# =============================

def rfid_menu():
	
    rfid_sketch_map = {
    "1": "rfid_card_reader.ino",
    "2": "rfid_uid_logger.ino",
    "3": "nfc_tag_analyzer.ino",
    "4": "nfc_ndef_parser.ino",
    "5": "nfc_signal_monitor.ino",
    "6": "rfid_frequency_tester.ino",
    "7": "tag_type_identifier.ino",
    "8": "nfc_data_dumper.ino",
    "9": "tag_emulation_lab.ino"
}

    while True:
        clear()
        print("""
======== RFID / NFC Research ========

[1] RFID Card Reader
[2] RFID UID Logger
[3] NFC Tag Analyzer
[4] NFC NDEF Parser
[5] NFC Signal Strength Monitor
[6] RFID Frequency Tester
[7] Tag Type Identifier
[8] NFC Data Dumper (Lab)
[9] Tag Emulation (Lab Only)
[0] Back
""")

        choice = input("Select: ")

if choice == "0":
    return

if choice in rfid_sketch_map:
    upload_sketch(rfid_sketch_map[choice])
else:
    print("Invalid Option")



# =============================
# Infrared Research
# =============================

def infrared_menu():
    while True:
        clear()
        print("""
======== Infrared Research ========

[1] IR Signal Recorder
[2] IR Signal Replayer (Own Devices)
[3] IR Protocol Analyzer
[4] IR Waveform Visualizer
[5] IR Frequency Tester
[6] IR Remote Database Builder
[7] IR Learning Mode
[0] Back
""")

        choice = input("Select: ")

        match choice:
            case "1":
                print("Recording IR signal...")
            case "2":
                print("Replaying IR signal...")
            case "3":
                print("Analyzing IR protocol...")
            case "4":
                print("Visualizing IR waveform...")
            case "5":
                print("Testing IR frequency...")
            case "6":
                print("Building IR remote database...")
            case "7":
                print("Learning IR remote...")
            case "0":
                return
            case _:
                print("Invalid Option")

        pause()


# =============================
# GPIO Tools
# =============================

def gpio_menu():
    while True:
        clear()
        print("""
======== GPIO / Hardware Testing ========

[1] GPIO Voltage Monitor
[2] PWM Signal Generator
[3] I2C Scanner
[4] SPI Device Detector
[5] UART Monitor
[6] ADC Sampler
[7] Logic Level Tester
[0] Back
""")

        choice = input("Select: ")

        match choice:
            case "1":
                print("Monitoring GPIO voltage...")
            case "2":
                print("Generating PWM signal...")
            case "3":
                print("Scanning I2C devices...")
            case "4":
                print("Detecting SPI devices...")
            case "5":
                print("Monitoring UART...")
            case "6":
                print("Sampling ADC...")
            case "7":
                print("Testing logic levels...")
            case "0":
                return
            case _:
                print("Invalid Option")

        pause()


# =============================
# Main Menu
# =============================

def main_menu():
    while True:
        clear()
        print("""


░██████████   ░██████   ░█████████   ░██████   ░██████  
░██          ░██   ░██  ░██     ░██ ░██   ░██ ░██   ░██ 
░██         ░██         ░██     ░██       ░██       ░██ 
░█████████   ░████████  ░█████████    ░█████    ░█████  
░██                 ░██ ░██               ░██  ░██      
░██          ░██   ░██  ░██         ░██   ░██ ░██       
░██████████   ░██████   ░██          ░██████  ░████████ 
                                                        
                                                        
=====================================
       FLIPPER ZERO CLI CLONE
=====================================

[1] WiFi Research
[2] BLE Research
[3] RFID / NFC Research
[4] Infrared Research
[5] GPIO / Hardware Testing
[6] Detect Port
[0] Exit
""")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                wifi_menu()
            case "2":
                ble_menu()
            case "3":
                rfid_menu()
            case "4":
                infrared_menu()
            case "5":
                gpio_menu()
            case "0":
                print("Exiting...")
                sys.exit()
            case _:
                print("Invalid Choice")
                pause()


if __name__ == "__main__":
    main_menu()

