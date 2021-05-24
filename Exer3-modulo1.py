import random



codigo = 112233
senha = int(input("Digite a senha :\n "))

while(senha != codigo ):
    print("Senha Invalida tente novamente")
    senha = int(input("Digite a senha :\n "))
        
while(senha == codigo):
    if senha == codigo:
        print("Parabens Voce Acertou!")
        break 
    else:
        print("Que pena você errou ,tente novamente!")

var_1 = "=*="   
var_2 = "OLA SEJA BEM VINDO !"
print(var_1*10)
print(var_2*1)
print(var_1*10)
print(" VAMOS TESTAR SUA SORTE")
print(var_1*10)

entrada=int(input("Digite um numero de 0 a 20 :\n")) 

num1= random.randrange(0,21)
contador=0

while(entrada != num1):

    if entrada > num1:
        print("o numero digitado é maior que o numero secreto")        
        entrada=int(input("Digite um numero de 0 a 20 :\n"))
        contador += 1
    elif entrada < num1:        
        print(" o numero digitado é menor que o numero secreto")
        entrada=int(input("Digite um numero de 0 a 20 :\n"))
        contador += 1

while(entrada == num1):
    print(f"PARABENS VOCE ACERTOU APOS {contador} TENTATIVAS!") 
    break       

















        
    
