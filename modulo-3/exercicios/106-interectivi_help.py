# from time import sleep


# c = ('\033[m',
#     '\033[1;100m',
#     '\033[1;30;103m',
#     '\033[1;101m',
#     '\033[1;102m'
#     )


# def i_help(funcao):
#     l(f'Acessando o manual da comando {fun}', 2)
#     sleep(0.5)
#     print(c[4], end="")
#     help(funcao)
#     print(c[0], end="")


# def l(msg, cor):
#     print(c[cor], end="")
#     print(f'~' * (len(msg) + 10))
#     print(f'{msg:^{len(msg) + 10}}')
#     print(f'~' * (len(msg) + 10))
#     print(c[0], end="")



# while True:
#     l('SEJA BEM VINDO AO PyHELP', 1)
#     fun = str(input('QUAL FUNÇÃO DESEJA RECEBER AJUDA: ')).lower()
#     if fun == 'fim':
#         brea
#     else:
#         i_help(fun)

    
    

# l('ATÉ LOGO', 3)



# Ex. 106 +=

fVerde, fAzul, fRoxo = "\033[1;30;42m", "\033[1;30;44m", "\033[1;30;45m"
normal = "\033[m"


def ajuda():
    while True:
        # Título
        print(fVerde, end="")
        print("~" * 30)
        print(" Sistema de ajuda para Python")
        print("~" * 30)
        print(normal)

        # Input
        comando = str(input("Comando ou biblioteca ('fim' para): "))

        # Condição de parada
        if comando.lower() == "fim":
            print(fRoxo, end="")
            print("~" * 16)
            print(" Até a próxima!")
            print("~" * 16)
            print(normal)
            break

        # Ajuda
        print(fAzul, end="")
        print(help(comando))
        print(normal)


ajuda()