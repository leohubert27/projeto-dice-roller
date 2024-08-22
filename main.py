import random

print("----------------------------------------------------------------------------------")
print("Bem vindos ao meu projeto em Python para rolagem de dados em Dungeons and Dragons!")
print("----------------------------------------------------------------------------------")
print("\n")

funcionando = True

while funcionando == True:
    total = 0
    lados = "a"
    rolagens = "a"

    while lados.isnumeric() == False:
        lados = input("Quantos lados o dado tem? ")
        if lados.isnumeric() == False:
            print("Você deve digitar um número!")
            continue
        elif int(lados) < 4:
            print("Você deve ter pelo menos 4 lados!")
            lados = "a"
    lados = int(lados)

    while rolagens.isnumeric() == False:
        rolagens = input("Quantas vezes deseja rolar os dados? ")
        if rolagens.isnumeric() == False:
            print("Você deve digitar uma número!")
            continue
        elif int(rolagens) < 1:
            print("Você deve rolar o dado pelo menos uma vez!")
            rolagens = "a"
    rolagens = int(rolagens)

    for x in range(rolagens):
       rolagens = random.randint (1,lados)
       total += rolagens
       print("Rolagem ", x+1, ": ", rolagens)
    print("Total: ", total)
    print("\n")

    jogar_novamente = input("Deseja rolar novos dados (S/N)? ")
    if jogar_novamente.upper() == "N":
        funcionando = False
    print ("\n")

print("Obrigado por jogar!")