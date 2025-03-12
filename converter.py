from PIL import Image
import binascii

def save_jpeg_data(combined_string):
    
    #Saves the combined JPEG hex ASCII data to a text file.
    with open("jpeg_hex_data.txt", 'w') as file:
        file.write(combined_string)
    
    print("JPEG hex data saved to jpeg_hex_data.txt")

def convert_hex_to_jpeg(hex_file="jpeg_hex_data.txt", output_image="output.jpg"):
    """
    Converts the hexadecimal ASCII data from a text file to a raw binary image and saves it as a JPEG.
    """
    try:
        # Read the hex data from the file
        with open(hex_file, 'r') as file:
            hex_data = file.read().strip()

        # Convert hex ASCII data to binary
        binary_data = binascii.unhexlify(hex_data)

        # Save binary data as a JPEG file
        with open(output_image, 'wb') as img_file:
            img_file.write(binary_data)

        print(f"JPEG image saved as {output_image}")

    except Exception as e:
        print(f"Error converting hex to JPEG: {e}")

def process_telemetry_data(ascii_data):
    
    # Process Telemetry Data
    telemetry_address_list = ascii_data[-1]
    telemetry_address_string = telemetry_address_list[0]

    print("\nTelemetry Address String:", telemetry_address_string)

    # Extract data fields
    internal_sync_tries = int(telemetry_address_string[9:11], 16)
    total_jpeg_bytes = int(telemetry_address_string[11:17], 16)
    stuffing = telemetry_address_string[17:49]

    input_voltage = round(int(telemetry_address_string[51:53], 16) * 0.02, 2)
    input_current = int(telemetry_address_string[53:55], 16)
    core_voltage = int(telemetry_address_string[55:57], 16) * 0.02
    core_current = int(telemetry_address_string[57:59], 16)

    flash_func = ['Flash OFF', 'Flash ON']
    flash_indicator = int(telemetry_address_string[61:62])

    baudrate_list = [
        '1200bps-8-n-1', '2400bps-8-n-1', '9600bps-8-n-1', '19200bps-8-n-1', 
        '38400bps-8-n-1', '57600bps-8-n-1', '115200bps-8-n-1', '230400bps-8-n-1', 
        '460800bps-8-n-1', '921600bps-8-n-1'
    ]
    baudrate_indicator = int(telemetry_address_string[62:63])

    fw_version = int(telemetry_address_string[63:65]) / 10.0

    # Print processed data
    print("\nProcessed Telemetry Data:")
    print("Number of internal communication sync tries:", internal_sync_tries)
    print("Total amount of JPEG image raw bytes:", total_jpeg_bytes)
    print("Stuffing String:", stuffing)
    print("Input Voltage:", input_voltage, "V")
    print("Input Current:", input_current, "mA")
    print("Core Voltage:", core_voltage, "V")
    print("Core Current:", core_current, "mA")
    print("Captured with", flash_func[flash_indicator])
    print("Baudrate mode used:", baudrate_list[baudrate_indicator])
    print("FW Version:", fw_version)
