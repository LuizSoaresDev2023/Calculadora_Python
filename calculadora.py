print("\nCALCULADORA EM PYTHON\nBy Luiz Soares, developer\n")
input("Pressione Enter para começar: ")
while True:
    try:
        operacao = int(input("\nEscolha uma operação para executar:\n1 - adição;\n2 - subtração;\n3 - multiplicação;\n4 - divisão;\nQualquer outro dígito:\n--- Encerrar calculadora!\n"))
    except ValueError:
        print ("\nPor favor, escolha uma opção válida! ")
        continue

    if operacao == 1:
        ad1 = int(input("\nDigite o primeiro número da adição! "))
        ad2 = int(input("Digite o segundo número da adição! "))
        adr = ad1 + ad2
        print(f'\nO resultado da adição de {ad1} com {ad2} é ===> {adr}. \n')
        input("Pressione Enter para retornar! ")
    elif operacao == 2:
        su1 = int(input("\nDigite o primeiro número da subtração! "))
        su2 = int(input("Digite o segundo número da subtração! "))
        sur = su1 - su2
        print(f'\nO resultado de {su1} menos {su2} é ===> {sur}. \n')
        input("Pressione Enter para retornar! ")
    elif operacao == 3:
        mu1 = int(input("\nDigite o primeiro número da multiplicação! "))
        mu2 = int(input("Digite o segundo número da multiplicação! "))
        mur = mu1 * mu2
        print(f'\nO resultado da multiplicação de {mu1} por {mu2} é ===> {mur}. \n')
        input("Pressione Enter para retornar! ")
    elif operacao == 4:
        di1 = int(input("\nDigite o primeiro número da divisão! "))
        di2 = int(input("Digite o segundo número da divisão! "))
        try:
            dire = di1 / di2
            print(f'\nO resultado da divisão de {di1} por {di2} é ===> {dire}. \n')
            input("Pressione Enter para retornar! ")
        except ZeroDivisionError:
            print(f'\nVocê tentou realizar uma divisão de {di1} por {di2}.\nNão é possível realizar divisão por zero!\n')
            input("Pressione Enter para retornar! ")
    else:
        print("\nPrograma encerrado! \nObrigado! Até a próxima!")
        print("Siga @luizsoares.designer.dev no Instagram! 🙂👍 ")
        input()
        break