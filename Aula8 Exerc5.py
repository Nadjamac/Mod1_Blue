

num = int(input("Digite um numero :\n"))
contador =  0

for x in range (1,num+1):
    if num % x == 0:
        print("{} é divisivel : {} ".format(num, num/x))
        contador += 1
if contador == 2: 
    print("é um numero primo ")  
else:
    print("não é um numero primo ")         


    



