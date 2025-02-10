def calculate_checksum(data, bit_size):
    """Calculate checksum for given bit size (8, 12, or 16)."""
    mask = (1 << bit_size) - 1
    return ~sum(data) & mask

def main():
    length = int(input("Enter the length of the data (up to 1024 bytes): "))
    if length > 1024:
        print("Input exceeds the maximum allowed size.")
        return

    # Collect data bytes with validation
    data = []
    for i in range(length):
        byte = int(input(f"Byte {i + 1}: "))
        if 0 <= byte <= 255:
            data.append(byte)
        else:
            print("Invalid byte value. Please enter a number between 0 and 255.")
            return

    # Select checksum type
    choice = int(input("Choose checksum type (1: 8-bit, 2: 12-bit, 3: 16-bit): "))
    bit_sizes = {1: 8, 2: 12, 3: 16}

    if choice in bit_sizes:
        checksum = calculate_checksum(data, bit_sizes[choice])
        print(f"{bit_sizes[choice]}-bit checksum: 0x{checksum:X}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
