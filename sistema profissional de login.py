## SISTEMA COM MENU BASICO 


def criar_usuario():
    print("\n== CRIACAO DE USUARIO ===")
    usuario = input("\n Defina um nome de usuario: ").strip().lower()
    senha = input("\n Insira nova senha: ").strip()
    print("\nUsuario criado com sucesso!")
    return usuario, senha 

def fazer_login(usuario, senha):
    tentativas = 0
    limite = 3
    
    while tentativas < limite: 
        print("\n AREA DE LOGIN")
        newusuario = input("\n Digite seu nome de usuario: ").strip().lower()
        newsenha = input("\n Digite sua senha: ").strip()

        if usuario != newusuario or senha != newsenha:
            tentativas += 1
            print("\n Usuario ou senha incorretos!")
            continue
        else:
            print(f"\n BEM VINDO {usuario}")
            exit()
        return True
    print("\n Limite de tentativas atingido!")
    print("\n VOLTANDO PARA CRIACAO DE USUARIO")
    return criar_usuario()

def menu():
    print("""
          MENU
          1 - Fazer Login
          2 - Criar usuario 
          3 - Sair""")
    return input("\n Escolha: ").strip()

def main():
    usuario = None
    senha = None

    while True:
        opcao = menu()
    
        if opcao == "1":
            print("\n CARREGANDO LOGIN")
            if usuario is None:
                print("\n Nenhum usuario criado. Crie um primeiro!")
                usuario, senha = criar_usuario()
                continue
            else:
                fazer_login(usuario, senha)
        elif opcao == "2":
            print("\n CARREGANDO CRIACAO DE USUARIO.")
            usuario, senha = criar_usuario()
        elif opcao == "3":
            print("\n Saindo...")
            break
        else :
            print("Opcao invalida.")

main()
