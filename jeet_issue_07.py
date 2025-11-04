def binary_to_decimal(binary_str):
    """Convert binary string to decimal integer"""
    try:
        return int(binary_str, 2)
    except ValueError:
        return "❌ Invalid binary number!"


def decimal_to_binary(decimal_num):
    """Convert decimal integer to binary string"""
    try:
        return bin(int(decimal_num))[2:]  # remove '0b' prefix
    except ValueError:
        return "❌ Invalid decimal number!"


# Main program
print("🔄 Binary ↔ Decimal Converter 🔄")
print("1️⃣ Binary → Decimal")
print("2️⃣ Decimal → Binary")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    binary = input("Enter a binary number: ")
    print(f"Decimal: {binary_to_decimal(binary)}")

elif choice == '2':
    decimal = input("Enter a decimal number: ")
    print(f"Binary: {decimal_to_binary(decimal)}")

else:
    print("❌ Invalid choice! Please enter 1 or 2.")
