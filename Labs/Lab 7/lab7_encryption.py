'''
Shefali Khatri, Tiffany Lastimosa, Netti Welsh, Gulnaz Saitgareeva
CS 5001, Fall 2020

The program encrypts and decrypts strings by Caesar Cipher.
'''


def encrypt(original_message, shift_amount):
    result = ""
    for letter in original_message:
        if 97 <= ord(letter) <= 122:
            position = ord(letter) - 96
            shifted_position = position + shift_amount
            if shifted_position > 26:
                resulting_letter = chr(shifted_position % 26 + 96)
                result += resulting_letter
            else:
                resulting_letter = chr(shifted_position + 96)
                result += resulting_letter
        else:
            result += letter
    return result


def decrypt(original_message, shift_amount):
    result = ""
    for letter in original_message:
        if 97 <= ord(letter) <= 122:
            position = ord(letter) - 96
            shifted_position = position - shift_amount
            if shifted_position < 1:
                resulting_letter = chr(shifted_position + 26 + 96)
                result += resulting_letter
            else:
                resulting_letter = chr(shifted_position + 96)
                result += resulting_letter
        else:
            result += letter
    return result


def validate_shift(shift_amount):
    if 0 <= shift_amount <= 25:
        return shift_amount
    else:
        return shift_amount % 25


def decrypt_unknown_message(message):
    combinations_list = []
    for i in range(1,6):
        shifted_message = decrypt(message, i)
        for j in range(1,6):
            new_message = shifted_message[-j:] + shifted_message[:-j]
            combinations_list.append(new_message)
    return combinations_list




def main():
    # message = input("Enter a message to encrypt: ").lower()
    # shift = int(input("Enter a shift amount: "))
    # validated_shift = validate_shift(shift)
    # print("Your super secret message is: {}".format(encrypt(message, validated_shift)))
    # encrypted_message = encrypt(message, validated_shift)
    # print("...decrypting encoded message now...")
    # print("It was: {}".format(decrypt(encrypted_message, shift)))
    print(decrypt_unknown_message("aqwuvwem, kp cp kphkpkvg nqqr, ykvj"))




if __name__ == "__main__":
    main()