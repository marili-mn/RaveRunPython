def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

def main():
    text = input("Ingresa un texto: ")

    if is_palindrome(text):
        print("El texto es palidromo")
    else:
        print("El texto no es palidromo")
main()