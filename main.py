alphabet_length = 26
alphabets = "abcdefghijklmnopqrstuvwxyz"
run_program = True

print("\n" + "="*90)
print("""\
 ██████╗███████╗ █████╗ ███████╗███████╗██████╗      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗
██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║     █████╗  ███████║███████╗█████╗  ██████╔╝    ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║     ██╔══╝  ██╔══██║╚════██║██╔══╝  ██╔══██╗    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
╚██████╗███████╗██║  ██║███████║███████╗██║  ██║    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
 ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝""")
print("="*90)
print("\n🔐 Cipher CLI Tool")
print("Encrypt and decrypt messages directly from your terminal.\n")


def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char in alphabets:
            char_index = alphabets.find(char)
            new_index = (char_index + key) % alphabet_length
            encrypted_text += alphabets[new_index]
        else:
            encrypted_text += char
    print("Encrypted text:", encrypted_text)

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char in alphabets:
            char_index = alphabets.find(char)
            new_index = (char_index - key) % alphabet_length
            decrypted_text += alphabets[new_index]
        else:
            decrypted_text += char
    print("Decrypted text:", decrypted_text)

while run_program:
    Choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    text = input("Enter the text: ").lower()

    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            break
        except ValueError:
            print("Invalid shift value. Please enter a number between 1 and 25.")

    if Choice == "e":
        print("\nEncrypting...")
        print()
        encrypt(text, shift)
    
    elif Choice == "d":
        print("\nDecrypting...")
        print()
        decrypt(text, shift)

    New_choice = input("\nDo you want to continue?(y/n):").lower()
    print()

    if New_choice == "n" or New_choice == "no":
        run_program = False
print("Thank you for using the Caesar Cipher Program! Goodbye!")
