# Générateur de Mot de Passe
Ce script Python permet de générer des mots de passe sécurisés en respectant certaines contraintes, telles que la longueur du mot de passe, le nombre de caractères spéciaux et le nombre de chiffres.

## Pré-requis
Python 3 🐍

## Utilisation
Clonez le projet dans votre environnement local :
```sh
git clone https://github.com/Antho-cs/Password_generator.git
cd Password_generator
```

Exécutez le script Python :
```shell
python generate_password.py
```

Suivez les invites pour saisir la longueur souhaitée du mot de passe, le nombre de caractères spéciaux et le nombre de chiffres.

Le mot de passe généré sera affiché à la fin, ou une erreur sera affichée si les contraintes ne sont pas satisfaites.

## Exemple d'utilisation
```sh
Saisie la taille voulue du mot de passe (1-100) : 12

Saisie le nombre de caractères spéciaux voulu : 2

Saisie le nombre de chiffres voulu : 2

Mot de passe généré : zF|X3qwG#m9o
```

## Contraintes
La longueur du mot de passe doit être supérieure ou égale à la somme des caractères spéciaux et des chiffres.
Le script utilise les bibliothèques standard random et string de Python.
## Auteur
CORNILLEAU Anthony
