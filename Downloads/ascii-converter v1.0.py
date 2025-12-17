# ascii_converter.py
import pyperclip  # om de ASCII output te kopiëren naar clipboard (pip install pyperclip)

ascii_alphabet = {
    'A': ["  ██  ", " █  █ ", "██████", "█    █", "█    █"],
    'B': ["█████ ", "█    █", "█████ ", "█    █", "█████ "],
    'C': [" █████", "█     ", "█     ", "█     ", " █████"],
    'D': ["█████ ", "█    █", "█    █", "█    █", "█████ "],
    'E': ["██████", "█     ", "█████ ", "█     ", "██████"],
    'F': ["██████", "█     ", "█████ ", "█     ", "█     "],
    'G': [" █████", "█     ", "█  ███", "█    █", " █████"],
    'H': ["█    █", "█    █", "██████", "█    █", "█    █"],
    'I': ["█████", "  █  ", "  █  ", "  █  ", "█████"],
    'J': ["  ████", "    █ ", "    █ ", "█   █ ", " ███  "],
    'K': ["█   █", "█  █ ", "███  ", "█  █ ", "█   █"],
    'L': ["█     ", "█     ", "█     ", "█     ", "██████"],
    'M': ["█    █", "██  ██", "█ ██ █", "█    █", "█    █"],
    'N': ["█    █", "██   █", "█ █  █", "█  █ █", "█   ██"],
    'O': [" ███ ", "█   █", "█   █", "█   █", " ███ "],
    'P': ["█████ ", "█    █", "█████ ", "█     ", "█     "],
    'Q': [" ███ ", "█   █", "█   █", "█  █ ", " ██ █"],
    'R': ["█████ ", "█    █", "█████ ", "█   █ ", "█    █"],
    'S': [" █████", "█     ", " ███  ", "     █", "█████ "],
    'T': ["██████", "  ██  ", "  ██  ", "  ██  ", "  ██  "],
    'U': ["█    █", "█    █", "█    █", "█    █", " ████ "],
    'V': ["█    █", "█    █", "█    █", " █  █ ", "  ██  "],
    'W': ["█    █", "█    █", "█ ██ █", "██  ██", "█    █"],
    'X': ["█    █", " █  █ ", "  ██  ", " █  █ ", "█    █"],
    'Y': ["█    █", " █  █ ", "  ██  ", "  ██  ", "  ██  "],
    'Z': ["█████", "   █ ", "  █  ", " █   ", "█████"],
    ' ': ["      ", "      ", "      ", "      ", "      "]
}

def text_to_ascii(text):
    text = text.upper()
    result = ["", "", "", "", ""]
    for char in text:
        if char in ascii_alphabet:
            for i in range(5):
                result[i] += ascii_alphabet[char][i] + "  "
        else:
            for i in range(5):
                result[i] += "      "  # lege ruimte voor onbekende tekens
    return "\n".join(result)

def main():
    print("ASCII Art Converter (Python)")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("Enter text: ")
        if user_input.lower() == 'exit':
            break
        ascii_result = text_to_ascii(user_input)
        print("\n" + ascii_result + "\n")
        
        # Vraag of je het wil kopiëren naar clipboard
        try:
            copy = input("Copy to clipboard? (y/n): ").lower()
            if copy == 'y':
                pyperclip.copy(ascii_result)
                print("Copied to clipboard!\n")
        except Exception as e:
            print(f"Clipboard copy failed: {e}\n")

if __name__ == "__main__":
    main()
