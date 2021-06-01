

frase =input("digite uma frase: \n").lower()
consoante= []
contador= 0

for item in frase:
    if item  not in "aeiou":
        consoante.append(item)
        contador += 1

print(f" Consoantes :{consoante}")  
print(f"contador: {contador}") 



