'''
См. предыдущую задачу, но вместо шифра Цезаря
использовать шифр Виженера.
'''
def vigenere_encrypt(plaintext, key):
    encrypted_text = []
    key = key.lower()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]

    for i in range(len(plaintext_int)):
        if plaintext[i].isalpha():
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            value += ord('A') if plaintext[i].isupper() else ord('a')
            encrypted_text.append(chr(value))
        else:
            encrypted_text.append(plaintext[i])

    return ''.join(encrypted_text)


def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key = key.lower()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]

    for i in range(len(ciphertext_int)):
        if ciphertext[i].isalpha():
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            value += ord('A') if ciphertext[i].isupper() else ord('a')
            decrypted_text.append(chr(value))
        else:
            decrypted_text.append(ciphertext[i])

    return ''.join(decrypted_text)


def main():
    message = input("Введите сообщение: ")
    choice = input("Введите 'e' для шифрования или 'd' для дешифрования: ")
    key = input("Введите ключ: ")

    if choice == 'e':
        print("Зашифрованное сообщение:", vigenere_encrypt(message, key))
    elif choice == 'd':
        print("Расшифрованное сообщение:", vigenere_decrypt(message, key))
    else:
        print("Неверный выбор. Пожалуйста, введите 'e' или 'd'.")


if __name__ == "__main__":
    main()