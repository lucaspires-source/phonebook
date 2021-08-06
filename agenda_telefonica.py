def adicionar():
    pass

def  alterar():
    pass

def excluir():
    pass

def buscar():
    pass

def listar():
    pass

def principal():
    while True:
        print("===Agenda Telefonica===")
        print("1 - Adicionar Contato")
        print("2 - Alterar Contato")
        print("3 - Excluir Contato")
        print("4 - Buscar Contato")
        print("5 - Listar Contato")
        print("6 - Sair")
        opcao = int(input("> "))
        if opcao == 1:
            adicionar()
        elif opcao == 2:
            alterar()
        elif opcao == 3:
            excluir()
        elif opcao == 4:
            buscar()
        elif opcao == 5:
            listar()
        elif opcao == 6:
            print("Saindo da agenda")
            break
        else:
            print("Opcao invalida. Por Favor, tente novamente.")