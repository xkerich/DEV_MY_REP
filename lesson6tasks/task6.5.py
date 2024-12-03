def cezar(txt, shag = 3):
    cezar_txt = ''
    for char in txt:
        if char.isalpha():
            shag_base = 65 if char.isupper() else 97
            char = chr((ord(char) - shag_base + shag) % 26 + shag_base)
        cezar_txt += char
    return cezar_txt

def cezar1(txt, shag = 3):
    cezar1_txt = ''
    for char in txt:
        if char.isalpha():
            shag_base = 65 if char.isupper() else 97
            char = chr((ord(char) - shag_base - shag) % 26 + shag_base)
        cezar1_txt += char
    return cezar1_txt

def main():
    txt = input('Введите текст: ')
    action = input('Выберите действие (шифровать/дешифровать): ').lower()
    if action == 'шифровать':
        result = cezar(txt)
    elif action == 'дешифровать':
        result = cezar1(txt)
    else:
        print('Неверное действие, попробуйте снова.')
        return
    print('Результат: ', result)
if __name__ == "__main__":
    main()
