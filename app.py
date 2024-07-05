def text_to_binary(text):
    """Convert a text string to its binary representation with spaces between each 8-bit segment."""
    binary_string = ' '.join(format(ord(char), '08b') for char in text)
    return binary_string

def binary_to_text(binary_string):
    """Convert a binary string to its text representation."""
    # Remove any spaces from the binary string
    binary_string = binary_string.replace(" ", "")
    
    # Ensure the binary string length is a multiple of 8
    if len(binary_string) % 8 != 0:
        raise ValueError("Invalid binary string length. It should be a multiple of 8.")

    binary_values = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    ascii_characters = [chr(int(binary, 2)) for binary in binary_values]
    return ''.join(ascii_characters)

def read_file(filename):
    """Read the content of a file."""
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    """Write content to a file."""
    with open(filename, 'w') as file:
        file.write(content)

def convert_file(filename, conversion_type):
    """Convert the content of a file based on the specified conversion type."""
    content = read_file(filename)
    
    if conversion_type == 'text_to_binary':
        converted_content = text_to_binary(content)
        output_filename = filename + ".bin"
    elif conversion_type == 'binary_to_text':
        converted_content = binary_to_text(content)
        output_filename = filename + ".txt"
    else:
        raise ValueError("Invalid conversion type. Use 'text_to_binary' or 'binary_to_text'.")
    
    write_file(output_filename, converted_content)
    print(f"File {filename} has been converted and saved as {output_filename}")

if __name__ == "__main__":
    import os
    
    filename = "sample.txt.bin"
    
    # Check if the file exists
    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist.")
    else:
        choice = input("Would you like to (t)ext to binary or (b)inary to text? ").strip().lower()
        
        if choice == 't':
            convert_file(filename, 'text_to_binary')
        elif choice == 'b':
            convert_file(filename, 'binary_to_text')
        else:
            print("Invalid choice. Please select 't' for text to binary or 'b' for binary to text.")
