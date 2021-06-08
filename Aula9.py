#Aula9.py

# Exercício 1 - Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem 
#corretamente a senha.

senha = "112233"
cod = input("digite a senha? \n")
while cod != senha:
   print("senha correta")
  cod = input("digite a senha? \n")
   break



