def reverse_text(text):
    reversed_text = text[::-1]
    return reversed_text

def main():
    
    user_input = input("Ingrese un texto: ")
    reversed_text = reverse_text(user_input)
    print("El texto al revés es:", reversed_text)

main()
