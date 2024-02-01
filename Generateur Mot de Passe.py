import random
import string

def generate_password(length, number_of_special_chars, number_of_digits):
    if length < number_of_special_chars + number_of_digits:
        raise ValueError("La longueur du mot de passe est inférieure à la somme minimale de caractères spéciaux et de chiffres.")

    # Générer des caractères spéciaux

    special_chars = string.punctuation
    password = ''.join(random.choice(special_chars) for _ in range(number_of_special_chars))

    # Générer des chiffres
    digits = string.digits
    password += ''.join(random.choice(digits) for _ in range(number_of_digits))

    # Remplir le reste avec des lettres (majuscules et minuscules)
    remaining_length = length - len(password)
    characters = string.ascii_letters
    password += ''.join(random.choice(characters) for _ in range(remaining_length))

    # Mélanger le mot de passe
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password


length = int(input("Saisie la taille voulue du mot de passe 1-100 : "))
num_special_chars = int(input("Saisie le nombre de caracteres spéciaux voulu : "))
num_digits = int(input("Saisie le nombre de chiffres voulu : "))

try:
    password = generate_password(length, num_special_chars, num_digits)
    print(password)
except ValueError as e:
    print(e)
