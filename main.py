import subprocess

def main():
    print("1. Decode")
    print("2. Encode")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        input_text = input("Enter the text to decode: ")

        # Base64 Decode
        try:
            base64 = subprocess.check_output(
                f'echo "{input_text}" | base64 -d', shell=True, text=True, stderr=subprocess.DEVNULL
            ).strip()
        except Exception:
            base64 = "Invalid Base64 input"

        # ROT13 Decode
        try:
            rot13 = subprocess.check_output(
                f'echo "{input_text}" | tr "A-Za-z" "N-ZA-Mn-za-m"', shell=True, text=True, stderr=subprocess.DEVNULL
            ).strip()
        except Exception:
            rot13 = "Invalid ROT13 input"

        # Hexadecimal Decode
        try:
            hexadecimal = subprocess.check_output(
                f'echo "{input_text}" | xxd -r -p', shell=True, text=True, stderr=subprocess.DEVNULL
            ).strip()
        except Exception:
            hexadecimal = "Invalid Hexadecimal input"

        # Binary Decode
        try:
            binary = subprocess.check_output(
                f'echo "{input_text}" | tr -d " " | perl -lpe \'$_=pack("B*",$_)\'',
                shell=True, text=True, stderr=subprocess.DEVNULL
            ).strip()
        except Exception:
            binary = "Invalid Binary input"

        # ASCII Decimal Decode
        try:
            ascii_dec = subprocess.check_output(
                f'echo "{input_text}" | awk \'{{for(i=1;i<=NF;i++)printf("%c", $i)}}\'',
                shell=True, text=True, stderr=subprocess.DEVNULL
            ).strip()
        except Exception:
            ascii_dec = "Invalid ASCII Decimal input"

        print(f"\nDecoded Results:")
        print(f"Base64     : {base64}")
        print(f"ROT13      : {rot13}")
        print(f"Hex        : {hexadecimal}")
        print(f"Binary     : {binary}")
        print(f"ASCII Dec  : {ascii_dec}")

    elif choice == '2':
        input_text = input("Enter the text to encode: ")

        # Base64 Encode
        base64 = subprocess.check_output(f'echo -n "{input_text}" | base64', shell=True, text=True).strip()

        # ROT13 Encode
        rot13 = subprocess.check_output(f'echo -n "{input_text}" | tr "A-Za-z" "N-ZA-Mn-za-m"', shell=True, text=True).strip()

        # Hexadecimal Encode
        hexadecimal = subprocess.check_output(f'echo -n "{input_text}" | xxd -p', shell=True, text=True).strip()

        # Binary Encode
        binary = subprocess.check_output(
            f'echo -n "{input_text}" | perl -lpe \'$_=unpack("B*",$_)\'',
            shell=True, text=True).strip()

        # ASCII Decimal Encode
        ascii_dec = " ".join(str(ord(c)) for c in input_text)

        print(f"\nEncoded Results:")
        print(f"Base64     : {base64}")
        print(f"ROT13      : {rot13}")
        print(f"Hex        : {hexadecimal}")
        print(f"Binary     : {binary}")
        print(f"ASCII Dec  : {ascii_dec}")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()