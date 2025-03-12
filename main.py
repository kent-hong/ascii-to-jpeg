from extractor import extract_data
from converter import process_telemetry_data, save_jpeg_data, convert_hex_to_jpeg

def main():
    # Extract ASCII and JPEG data
    transmitted_ascii_data, ascii_data, jpeg_stored_data = extract_data()

    print("\nTransmitted Ascii Data Excluding End Marker:", ascii_data)

    print("\nJPEG Data List:", jpeg_stored_data)

    # Combine JPEG data from master list into one string variable and save it
    combined_jpeg_string = "".join(jpeg_stored_data)
    save_jpeg_data(combined_jpeg_string)

    # Convert hex data to JPEG image
    convert_hex_to_jpeg()

    # Process telemetry data
    process_telemetry_data(ascii_data)

if __name__ == "__main__":
    main()
