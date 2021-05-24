
#INVESTIGANDO UM CRIME !

n="NAO"
s="SIM"
sim = 0

q1 = input("Telefonou para a vítima? Digite s para Sim n para Não : \n" )    
q2 = input("Esteve no local do crime? Digite s para Sim n para Não :  \n") 
q3 = input("Já trabalhou com a vítima? Digite s para Sim n para Não :  \n")
q4 = input("Mora perto da vítima? Digite s para Sim n para Não :  \n")
q5 = input("Devia para a vítima? Digite s para Sim n para Não :  \n")

L=[q1,q2,q3,q4,q5]

for item in L:
    if item == s:
        sim += 1
        if sim <=2: 
            print( "CONSIDERADO SUSPEITO")
        elif sim >=3  or sim <=4:
            print(" CONSIDERADO CUMPLICE ") 
        elif sim == 5:
            print("ASSASINO")
        else:
            print("CONSIDERADO INOCENTE")  