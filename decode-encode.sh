#!/bin/bash
# filepath: main.sh

echo "1. Decode"
echo "2. Encode"
read -p "Enter your choice (1 or 2): " choice

if [[ "$choice" == "1" ]]; then
    read -p "Enter the text to decode: " input_text

    # Base64 Decode
    base64_dec=$(echo "$input_text" | base64 -d 2>/dev/null)
    [[ $? -ne 0 ]] && base64_dec="Invalid Base64 input"

    # ROT13 Decode
    rot13_dec=$(echo "$input_text" | tr 'A-Za-z' 'N-ZA-Mn-za-m')

    # Hexadecimal Decode
    hex_dec=$(echo "$input_text" | xxd -r -p 2>/dev/null)
    [[ $? -ne 0 ]] && hex_dec="Invalid Hexadecimal input"

    # Binary Decode
    binary_dec=$(echo "$input_text" | tr -d ' ' | perl -lpe '$_=pack("B*",$_)' 2>/dev/null)
    [[ $? -ne 0 ]] && binary_dec="Invalid Binary input"

    # ASCII Decimal Decode
    ascii_dec=$(echo "$input_text" | awk '{for(i=1;i<=NF;i++)printf("%c", $i)}')
    [[ -z "$ascii_dec" ]] && ascii_dec="Invalid ASCII Decimal input"

    echo
    echo "Decoded Results:"
    echo "Base64     : $base64_dec"
    echo "ROT13      : $rot13_dec"
    echo "Hex        : $hex_dec"
    echo "Binary     : $binary_dec"
    echo "ASCII Dec  : $ascii_dec"

elif [[ "$choice" == "2" ]]; then
    read -p "Enter the text to encode: " input_text

    # Base64 Encode
    base64_enc=$(echo -n "$input_text" | base64)

    # ROT13 Encode
    rot13_enc=$(echo -n "$input_text" | tr 'A-Za-z' 'N-ZA-Mn-za-m')

    # Hexadecimal Encode
    hex_enc=$(echo -n "$input_text" | xxd -p)

    # Binary Encode
    binary_enc=$(echo -n "$input_text" | perl -lpe '$_=unpack("B*",$_)')

    # ASCII Decimal Encode
    ascii_enc=$(echo -n "$input_text" | od -An -t u1 | tr -s ' ' | sed 's/^ *//;s/ *$//')

    echo
    echo "Encoded Results:"
    echo "Base64     : $base64_enc"
    echo "ROT13      : $rot13_enc"
    echo "Hex        : $hex_enc"
    echo "Binary     : $binary_enc"
    echo "ASCII Dec  : $ascii_enc"
else
    echo "Invalid choice. Please enter 1 or 2."
fi
