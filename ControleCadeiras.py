# SISTEMA DE CADEIRAS HOSPITAL DAS CLINICAS.

# --------------------
# VARIAVEIS E LISTAS
# --------------------

# Lista com os IDs das cadeiras disponíveis
cadeiras_disponiveis = [1, 2, 3, 4, 5]

# Lista com os IDs das cadeiras em uso
cadeiras_em_uso = []

# Lista com os nomes de quem está usando cada cadeira
nomes_usuarios = []

# Lista com os CPFs de quem esta usando cada cadeira
cpfs_usuarios = []

# ------------
# FUNCOES
# ------------

# Função do menu
def mostrar_menu():
    print("")
    print("=== SISTEMA DE CADEIRAS DE RODAS ===")
    print("1 - Retirar cadeira")
    print("2 - Devolver cadeira")
    print("3 - Listar cadeiras")
    print("4 - Sair")
    print("=====================================")


# Função de lista das cadeiras
def listar_cadeiras():
    print("")
    print("--- CADEIRAS DISPONÍVEIS ---")

    # Se a lista estiver vazia surgira uma mensagem avisando ao usuario.
    if len(cadeiras_disponiveis) == 0:
        print("Nenhuma cadeira disponível no momento.")
    else:
        for id_cadeira in cadeiras_disponiveis:
            print("Cadeira", id_cadeira, "- Disponível")

    print("")
    print("--- CADEIRAS EM USO ---")

    if len(cadeiras_em_uso) == 0:
        print("Nenhuma cadeira em uso no momento.")
    else:
        # Range aqui é usado para acessar o índice e pegar nome/cpf correspondente
        for i in range(len(cadeiras_em_uso)):
            print("Cadeira", cadeiras_em_uso[i], "- Em uso por:", nomes_usuarios[i], "| CPF:", cpfs_usuarios[i])


# Função para retirar uma cadeira
def retirar_cadeira():
    print("")
    print("--- RETIRADA DE CADEIRA ---")

    # Verifica se tem cadeiras disponíveis
    if len(cadeiras_disponiveis) == 0:
        print("Não há cadeiras disponíveis no momento.")
        return

    # Mostra as opções disponíveis
    print("Cadeiras disponíveis:", cadeiras_disponiveis)

    # Pede os dados do usuário
    # Pede o nome, só aceita letras e espaços
    nome = input("Nome do paciente ou colaborador: ")
    while nome.replace(" ", "").isalpha() == False or nome.strip() == "": # Faz aceitar apenas letras e espaço.
        print("Nome inválido! Digite apenas letras, sem números ou símbolos.")
        nome = input("Nome do paciente ou colaborador: ")

    # Coloca a primeira letra de cada palavra em maiuscula usando a função "Title"
    nome = nome.title()

    # Pede o CPF e valida: só aceita exatamente 11 números
    cpf = input("CPF (somente números): ")
    while cpf.isdigit() == False or len(cpf) != 11:
        print("CPF inválido! Digite exatamente 11 números, sem pontos ou traços.")
        cpf = input("CPF (somente números): ")

    # Formata o CPF no padrão 000.000.000-00
    cpf = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11]

    id_cadeira = int(input("Número da cadeira desejada: ")) # Pede para que o ususario informe qual o numero da cadeira que ele deseja (so pode numeros que estão disponiveis)

    # Verifica se o número informado está na lista de disponíveis
    if id_cadeira in cadeiras_disponiveis:
        # Remove da lista de disponíveis
        cadeiras_disponiveis.remove(id_cadeira)

        # Adiciona nas listas de "em uso"
        cadeiras_em_uso.append(id_cadeira)
        nomes_usuarios.append(nome)
        cpfs_usuarios.append(cpf)

        print("Cadeira", id_cadeira, "retirada com sucesso por", nome)
    else:
        print("Cadeira", id_cadeira, "não está disponível.")


# Função para devolver uma cadeira
def devolver_cadeira():
    print("")
    print("--- DEVOLUÇÃO DE CADEIRA ---")

    if len(cadeiras_em_uso) == 0:
        print("Nenhuma cadeira está em uso no momento.") # Caso nenhuma cadeira esteja em uso ira aparecer esta mensagem.
        return

    print("Cadeiras em uso:", cadeiras_em_uso)

    id_cadeira = int(input("Número da cadeira a devolver: "))

    # Verifica se a cadeira está na lista de em uso
    if id_cadeira in cadeiras_em_uso:
        # Descobre a posição da cadeira na lista para remover nome e cpf também
        posicao = cadeiras_em_uso.index(id_cadeira)

        # Remove das listas de "em uso"
        cadeiras_em_uso.remove(id_cadeira)
        nomes_usuarios.pop(posicao)
        cpfs_usuarios.pop(posicao)

        # Devolve para a lista de disponíveis
        cadeiras_disponiveis.append(id_cadeira)

        print("Cadeira", id_cadeira, "devolvida com sucesso!")
    else:
        print("Essa cadeira não está registrada como em uso.")


# -----------------
# MENU DO PROGRAMA
# -----------------

print("Bem-vindo ao sistema de controle de cadeiras de rodas!")

opcao = ""

while opcao != "4":
    mostrar_menu()
    opcao = input("Digite sua opção: ")

    if opcao == "1":
        retirar_cadeira()

    elif opcao == "2":
        devolver_cadeira()

    elif opcao == "3":
        listar_cadeiras()

    elif opcao == "4":
        print("Sistema encerrado. Até logo!")

    else:
        print("Opção inválida. Tente novamente.")