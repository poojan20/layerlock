# Function to convert binary to text
def binary_to_text(binary_file_path, output_file_path):
    with open(binary_file_path, 'r') as binary_file:
        binary_data = binary_file.read().strip()  # Read binary data from file

    text_data = ''
    for i in range(0, len(binary_data), 8):  # Process binary data in chunks of 8 bits
        byte = binary_data[i:i+8]  # Get the next 8 bits
        decimal_value = int(byte, 2)  # Convert binary to decimal
        character = chr(decimal_value)  # Convert decimal to ASCII character
        text_data += character

    with open(output_file_path, 'w') as output_file:
        output_file.write(text_data)  # Write text data to output file
'''
# Example usage:
binary_file_path = "D:\output_binary_data.txt"
output_file_path = "D:\output_data.txt"

binary_to_text(binary_file_path, output_file_path)
print("Text data written to:", output_file_path)
'''

# Function to convert text to binary
def text_to_binary(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()
            binary_text = ' '.join(format(ord(char), '08b') for char in text)

        with open(output_file, 'w') as file:
            file.write(binary_text)

        print(f"Text from '{input_file}' successfully converted to binary and saved in '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
'''
# Input and Output file names
input_file_name = "D:\output_binary_data.txt"
output_file_name = "D:\output_text_bi.txt"

# Convert the text file to binary
text_to_binary(input_file_name, output_file_name)
'''