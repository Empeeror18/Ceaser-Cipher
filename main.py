encrypt():   
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value (1-25): "))
    encrypted_text = ""
    for char in text:
        if char.find(" ") != -1:
            encrypted_text += char
