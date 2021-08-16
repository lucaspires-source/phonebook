
def salvar_contatos(lista):
    arquivo = open("contatos.txt","w")
    for contato in lista:
        arquivo.write("{},{},{},{},{}\n".format(contato['nome'],contato['telefone'],contato['email'],contato['facebook'],contato['twitter'],))
    arquivo.close()

def carregar_contatos():
    lista =[]

    try:
        arquivo = open("contatos.txt","r")
        for linha in arquivo.readlines():
            coluna = linha.strip().split(",")
            contato = {
                "nome":coluna[0],
                "telefone":coluna[1],
                "email":coluna[2],
                "facebook":coluna[3],
                "twitter":coluna[4],
            }
            lista.append(contato)
        arquivo.close()
    except FileNotFoundError:
        pass
    return  lista
def existe_contato(nome,lista):


    if len(lista) >0:
        for contato in lista:
            if contato["nome"] == nome:
                return True
            else:
                return False
def adicionar(lista):
    while True:

        nome = input("Digite o nome do contato:")
        if not existe_contato(nome, lista):
            break
        else:
            print("Esse email ja foi utilizado,por favor tente novamente")
    contato = {
        "nome": nome,
        "telefone": input("Digite o numero de telefone do contato: "),
        "email": input("Digite o e-mail do contato: "),
        "facebook": input("Digite o usuario de Facebook do contato:"),
        "twitter": input("Digite o o usuario de Twitter do contato:")
    }

    lista.append((contato))
    print("o contato foi cadastrato com sucesso\n".format(contato["nome"]))
def  alterar():
    pass

def excluir():
    pass

def buscar(lista):
    if len(lista)> 0:
        nome = input("Digite o nome do contato a ser encontratado:")
        if existe_contato(nome,lista):
            for contato in lista:
                if contato['nome'] == nome:
                    print("\tNome:",format(contato["nome"]))
                    print("\tTelefone:", format(contato["telefone"]))
                    print("\tEmail:", format(contato["email"]))
                    print("\tFacebook:",format(contato["facebook"]))
                    print("\tTwitter:", format(contato["twitter"]))
        else:
            print("Não existe contato cadastrado no sistema com o nome {}".format(nome))
    else:
        print("Nao existe nenhum contrato cadastrado no sistema")

def listar(lista):
    if len(lista)> 0:
        for i, contato in enumerate(lista):
            print("Contato".format(i+1))
            print("\tNome:",format(contato["nome"]))
            print("\tTelefone:", format(contato["telefone"]))
            print("\tEmail:", format(contato["email"]))
            print("\tFacebook:",format(contato["facebook"]))
            print("\tTwitter:", format(contato["twitter"]))
    else:
        print("Nao existe nenhum contrato cadastrado no sistema")
def principal():
    lista = carregar_contatos()
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
            salvar_contatos(lista)
        elif opcao == 2:
            alterar()
            salvar_contatos(lista)
        elif opcao == 3:
            excluir()
            salvar_contatos(lista)
        elif opcao == 4:
            buscar(lista)
        elif opcao == 5:
            listar(lista)
        elif opcao == 6:
            print("Saindo da agenda")
            break
        else:
            print("Opcao invalida. Por Favor, tente novamente.")



principal()