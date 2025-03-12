import serial

def extract_data():
    # Replace 'COMX' with the actual COM port of your Bluetooth / UART device
    ser = serial.Serial('COM11', baudrate=9600, timeout=1)

    # Masterlist for holding all data in lists
    transmitted_ascii_data = []
    ascii_data = []
    jpeg_stored_data = []

    # Read data from UART
    while True:
        response = ser.readline()
        decoded_response = response.decode('utf-8').strip()  # Decode once

        # Skip empty responses
        if not decoded_response:
            continue

        # Print the response
        print(decoded_response)

        # Create a separate list for each response and append to ascii_data list
        separate_list = [decoded_response]
        transmitted_ascii_data.append(separate_list)

        # Break the loop if the response signals end of transmission
        if decoded_response == "End of Transmission":
            break

    ser.close()

    # Process extracted data
    for individual_ascii_data_list in transmitted_ascii_data:
        if individual_ascii_data_list[0] != "End of Transmission": # Exclude the end marker
            ascii_data.append(individual_ascii_data_list) # Store ascii data with excluded end marker
            ascii_string = individual_ascii_data_list[0] # Extract the string

            # Extract indexing slices
            current_sentence = ascii_string[1:5]
            print("Current Sentence:", current_sentence)

            jpeg_data = ascii_string[9:65] # Store the slice in jpeg_data
            print("JPEG data:", jpeg_data)
            jpeg_stored_data.append(jpeg_data) # Store JPEG data in JPEG Master list

            telemetry_address = ascii_string[5:9]
            print("Telemetry Sentence Address:", telemetry_address)

    return transmitted_ascii_data, ascii_data, jpeg_stored_data
