
##SISTEMA DE LOGIN COM USUARIO SENHA / FORMATACAO CORRETA / FAIL FAST /
## EVITAR REPETICAO


while True:

# criacao de usuario       
    novo_usuario = input("Digite seu novo usuario: ").strip().lower()
    nova_senha = input("Digite sua nova senha: ").strip()


    print("\nUsuario criado com sucesso!\n")
    
    #LIMITE DE TENTATIVAS
    tentativas = 0
    limite = 3
    
    #  tentativa de login
    while tentativas < limite:
        print("FACA LOGIN AGORA")

        usuario_login = input("Digite seu usuario: ").strip().lower()
        senha_login = input("Digite sua senha: ").strip()

        erro = False

    #VERIFICANDO USUARIO
        if usuario_login != novo_usuario:
            print("Usuario invalido.\n")
            erro = True
            
        if senha_login != nova_senha:
            print("Senha incorreta.\n")
            erro = True
        if erro:
            print("Tente novamente!")
            tentativas += 1
            continue

        print("ACESSO PERMITIDO!")
        exit()
    print("\nConta bloqueada por excessos de tentativas.")
    print("Crie uma nova conta para continuar.\n")

