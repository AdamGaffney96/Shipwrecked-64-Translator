def decode(string: str) -> str:
    string = string.lower()
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    decoded_string: str = ""
    for letter in string:
        letter_index = alphabet.find(letter)
        if letter not in alphabet:
            decoded_string += letter
        elif letter_index % 2 == 0:
            decoded_string += alphabet[letter_index+1]
        else:
            decoded_string += alphabet[letter_index-1]
    return decoded_string

def main(message: str) -> None:
    decoded_message = decode(message)
    print(f"The input message was '{message}'. The encoded/decoded message is '{decoded_message}'")
    
if __name__ == "__main__":
    print("===========================================")
    print("Welcome to the Shipwrecked 64 text decoder!")
    print("===========================================")
    print("Note that both encoding and decoding a message use the same cypher.\n")
    while True:
        message = input("What message would you like to decode/encode: ")
        main(message)
        another = input("Would you like to decode another message (y/n)? ").lower()
        if (another == "n" or another == "n"):
            input("Press Enter to close.")
            break