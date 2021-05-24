
#02 - Utilizando estruturas de repetição com variável de controle, 
#faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece
#s vogais a,e,i,o,u e mostre na tela, 
# depois mostre na tela essa mesma frase sem nenhuma vogal.


print()
user=("=*=")
print(10 * user)
print("      BEM VINDO ! ")
print(10 * user)
print()

vogais = ("a","e","i","o","u")
consoante= ["b","c","d","f","h","g","j","l","m","n","p","q","r","s","t","w","y","x","z"]
frase = input("Este programa é inteligente e vamos contar vogais de sua frase.Digite aqui sua frase: \n").lower()
print("O resultado é","\n vogal a:",frase.count("a"),"\n vogal e:",frase.count("e"),"\n vogal i:",frase.count("i"),"\n vogal 0:",frase.count("o"),"\n vogal u:",frase.count("u"))
print("Sua frase sem vogais é :" ,frase.replace("a",'').replace("e",'').replace("i",'').replace("o",'').replace("u",''))
letra = []
contador = 0
for item in frase:
   if item in "aeiou":
      contador +=1
print(f" a sua frase possui {contador} vogais" )         

  

  




 

   

