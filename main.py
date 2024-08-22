import random

print("----------------------------------------------------------------------------------")
print("Bem vindos ao meu projeto em Python para rolagem de dados em Dungeons and Dragons!")
print("----------------------------------------------------------------------------------")
print("\n")

funcionando = True #cria o looping para iniciar o programa

while funcionando == True:
    total = 0
    lados = "a"
    rolagens = "a"

    #define as variáveis lados e rolagens como sentinela, para previnir que o usuário quebre o programa

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

    #cria o laço for para mostrar as rolagens de dados
    for x in range(rolagens):
       rolagens = random.randint (1,lados)
       total += rolagens
       print("Rolagem ", x+1, ": ", rolagens)
       print("\n")
    
    #pergunta ao usuário se ele deseja ver a soma das rolagens que fez
    ver_total = input("Deseja ver a soma dos dados (S/N)? ")
    if ver_total.upper() == "S":
        print("Soma total: ", total)
        print("\n")

    #pergunta ao usuário se ele deseja iniciar o looping novamente
    jogar_novamente = input("Deseja rolar novos dados (S/N)? ")
    if jogar_novamente.upper() == "N":
        funcionando = False
    print ("\n")

print("Obrigado por jogar!")