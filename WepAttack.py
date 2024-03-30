def xor_strings(a, b):
    # Function to XOR the strings of binary
    return ''.join(str(int(char_a) ^ int(char_b)) for char_a, char_b in zip(a, b))

def generate_all_xors(data):
    # Here I generate XORs for all possible pairs in the data
    result = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            result.append(xor_strings(data[i], data[j]))
    return result

def main():
    messages = [
        "11111111000000001111111100000000",
        "01010101010101010101010101010101",
        "11011101001011101100001000111010",
        "01101101101101101110111010010100",
        "11110001111100101111000010000000",
        "00001111000011110000111100001111",
        "11111111111111110000000000000000",
        "00010001111110110001111001110110",
        "10101110011101100111011011110001",
        "01111111110111110111100001110111",
    ]
    ciphertexts = [
        "00010111011000110010010110100011",
        "11001101001111101100100011000110",
        "10100111111110110000100100001101",
        "01100100001110111001000101101000",
        "00110101010011010001100010011001",
        "10110101100100101001111111101110",
        "00111011101111110001011100011001",
        "11011011101101101111100111101111",
        "00110101101100101110011110011001",
    ]

    # Generate XOR combinations for messages and ciphertexts
    message_xors = generate_all_xors(messages)
    ciphertext_xors = generate_all_xors(ciphertexts)

    # Matching XORs between messages and ciphertexts
    matches = set(message_xors) & set(ciphertext_xors)  # Find common elements
    x = 0
    for match in matches:
        print(f"Matching XOR found: {match}")
        x+=1
    print(f"Number of matches: {x}")

if __name__ == "__main__":
    main()
