from Alphabet import alphabet
from Art import logo

#------------------------------------------------
def caesar(message, shift_level, shift_direction):
    cipher_text = ''

    # reverse direction of shift if we are decoding a message
    if shift_direction == 'decode':
        shift_level *= -1

    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_level

            #avoid going off the end of the list
            while (new_position < 0):
                new_position += 26
            while (new_position > 25): 
                new_position -= 26
            
            new_char = alphabet[new_position]
            cipher_text += new_char
        else:
            cipher_text += char

    print(f'the {shift_direction}d text is {cipher_text}')

#------------------------------------------------
print(logo)
should_continue = True

while should_continue:
    direction = ''
    while direction != 'encode' and direction != 'decode':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

    plain_text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    caesar(plain_text, shift, direction)

    user_continue = input('continue?(y,n): ').lower()

    if user_continue == 'n':
        should_continue = False
                          
print('Closing Caeser Cipher')