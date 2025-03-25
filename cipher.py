import string

message_type = int(input('Please select one of two options\n 1. Encryption\n 2. Decryption\n'))
message = input('Please enter your message: ')
key = 4

alphabet = list(string.ascii_lowercase)

# Makes sure that the user can only enter 1 or 2, and will continuously get prompted otherwise
while message_type not in (1, 2):
    print('Incorrect input, please enter 1 or 2')
    message_type = int(input('1. Encryption\n2. Decryption\n'))

direction = 1 if message_type == 1 else -1

# If user enters an empty message, or a message full of spaces, they will continuously get prompted to enter a proper message
while True:
    if message.strip():
        break
    print('Invalid message, please try again')
    message = input()

# For every iteration of the loop (length of the message) it first checks if the letter is in the alphabet, if so it assigns the index to the letter in the alphabet of the letter in message to a variable (alpha_index), then assigns the letter in the alphabet moved (either forwards or backwards) 'key' indicies (4), then finally adding the letter to the encrypted_message variable. If the element at message[i] is not in the alphabet (such as spaces) it gets added to encrypted_message
def cipher(direction):
    encrypted_message = ''
    for i in range(len(message)):
        if message[i] in alphabet:
            alpha_index = alphabet.index(message[i])
            encrypt_char = (alpha_index + (key * direction)) % 26
            encrypted_message += alphabet[encrypt_char]
        else:
            encrypted_message += message[i]

    return encrypted_message

# Depending on message_type, the appropriate function will run returning the message
if message_type == 1:
    print(f'Encrypted Message: {cipher(direction)}')
else:
    print(f'Decrypted Message: {cipher(direction)}')




