from random import randrange


def existe_contato(email,lista):
    if len(lista) >0:
        for contato in lista:
            if contato["email"] == email:
                return True
    return False
def adicionar(lista):
    while True:
        email = input("Digite o e-mail do contato: ")
        if not existe_contato(email,lista):
            break
        else:
            print("Esse email ja foi utilizado,por favor tente novamente")
    contato = {
        "id":str(randrange(1000)),
        "email": email,
        "nome": input("Digite o nome do contato:"),
        "facebook": input("Digite o usuario de Facebook do contato:"),
        "twitter": input("Digite o o usuario de Twitter do contato:")
    }

    lista.append((contato))
    print("o contato foi cadastrato com sucesso\n".format(contato["nome"]))
def  alterar():
    pass

def excluir():
    pass

def buscar():
    pass

def listar():
    pass

def principal():
    lista = []
    while True:
        print("=== Bem vindo a sua Agenda de contatos===")
        print("1 - Adicionar Contato")
        print("2 - Alterar Contato")
        print("3 - Excluir Contato")
        print("4 - Buscar Contato")
        print("5 - Listar Contato")
        print("6 - Sair")
        opcao = int(input("> "))
        if opcao == 1:
            adicionar(lista)
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



principal()