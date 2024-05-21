import random

def exibir_tudo():
    file = open("tudo.txt", "r")
    print(file.read())
    file.close()
    return

def exibir_por_pais():
    pais = input("digite o pais do qual deseja ver as receitas: ").lower()
            
    file = open("tudo.txt", "r")
            
    for linha in file:
        if f"{pais}|" in linha:
            print(linha)
    file.close()        
    return

def exibir_favoritos():
    file = open("favoritos.txt", "r")
    print(file.read())
    file.close()
    return

def exibir_ingrediente():
    ingrediente = input("Digite o ingrediente do qual deseja ver as receitas: ").lower()

    file = open("tudo.txt", "r")

    for linha in file:
        if (ingrediente) in linha:
            print(linha)
    file.close()
    return

def exibir_aleatorio():
    file = open("tudo.txt", "r")
            
    ret = []
    for linha in file:
        ret.append(linha)
                
    aleatorio = random.randint(0, len(ret)-1)
            
    print(ret[aleatorio])
    file.close()
    return

def alterar_adicionar():
    pais = input("Digite o país de origem da nova receita: ").lower()
    nome = input("Digite o nome da receita: ").lower()
    preparo = input("Digite o preparo da receita com os ingredientes: ").lower()
    novareceita = (f"{pais}|{nome}|{preparo}\n")
            
    file = open("tudo.txt", "a")
    file.write(novareceita)
    file.close()
    
    favoritos = input("""
deseja adicionar a receita aos favoritos?
[1] sim
[2] não
""")
    
    continuar = input("""
deseja continuar adicionando? 
[1] sim
[2] não
""")

    if continuar == "1":
        alterar_adicionar()

    elif continuar == "2":
        print("========================================================")        
            
    if favoritos == "1":
        file = open("favoritos.txt", "a")
        file.write(novareceita)
        file.close()    
    return

def alterar_remover():
    receita = input ("Digite o nome da receita que irá ser removida: ").lower()
            
    file = open("tudo.txt", "r")
    linhas = file.readlines()
    file.close()
            
    file_remover = open("tudo.txt", "w")
    for linha in linhas:
        if f";{receita};" not in linha:
            file_remover.write(linha)

    file_remover.close()

    file = open("favoritos.txt", "r")
    linhas = file.readlines()
    file.close()

    file_remover = open("favoritos.txt", "w")
    for linha in linhas:
        if receita not in linha:
            file_remover.write(linha)
            
    file_remover.close()                         
    return
def alterar_editar():
    receita = input("Digite qual receita será editada: ").lower()
    file = open("tudo.txt", "r")
    file_ler = file.readlines()
    file.close()

    linha_separada = None
    for linha in file_ler:
        if (f"|{receita}|") in linha:
            linha_separada = linha.strip().split("|")
            pais = input("Digite o novo nome do país da receita: ").lower()
            nome = input("Digite o novo nome da receita: ").lower()
            preparo = input("Digite o novo preparo e os ingredientes da receita: ").lower()
            if pais:
                linha_separada[0] = pais
            if nome:
                linha_separada[1] = nome
            if preparo:
                linha_separada[2] = preparo
            break

    if linha_separada:
        nova_linha = f"{linha_separada[0]}|{linha_separada[1]}|{linha_separada[2]}\n"

        file_editar = open("tudo.txt", "w")
        for linha in file_ler:
            if (f"|{receita}|") not in linha:
                file_editar.write(linha)
        file_editar.write(nova_linha)
        file_editar.close()

        file_favoritos = open("favoritos.txt", "r")
        linhas = file_favoritos.readlines()
        file_favoritos.close()

        file = open("favoritos.txt", "w")
        for linha in linhas:
            if (f"|{receita}|") not in linha:
                file.write(linha)

        favorito = input("""
Deseja adicionar a nova receita aos favoritos? 
[1] Sim
[2] Não
""")
        if favorito == "1":
            file.write(nova_linha)
        file.close()

        print("========================================================")
    else:
        print("Receita não encontrada.")

while True:
    opcao = input("""
Exibir -------> E
Alterar ------> A
Encerrar -----> X                  

Digite a funcionalidade desejada: """)
    
    if opcao == "E" or opcao == "e":
        funcionalidade_exibir = input("""                            
Como deseja exebir as receitas?
[1] Tudo 
[2] Por país 
[3] Favoritos 
[4] Aleatório
[5] Por ingrediente
[X] Voltar
""")
        if funcionalidade_exibir == "1":
            exibir_tudo()

        elif funcionalidade_exibir == "2":
            exibir_por_pais()

        elif funcionalidade_exibir == "3":
            exibir_favoritos()  

        elif funcionalidade_exibir == "4":
            exibir_aleatorio()

        elif funcionalidade_exibir == "5":
            exibir_ingrediente()
            
        elif funcionalidade_exibir == "X" or funcionalidade_exibir == "x":
            print("========================================================")        

    elif opcao == "A" or opcao == "a":
        funcionalidade_alterar = input("""
Como deseja deseja alterar uma receita?
[1] Adicionar 
[2] Remover 
[3] Editar
[X] Voltar
""" )
        if funcionalidade_alterar == "1":
            alterar_adicionar()

        elif funcionalidade_alterar == "2":
            alterar_remover()
        elif funcionalidade_alterar == "3":
            alterar_editar()

        elif funcionalidade_alterar == "X" or funcionalidade_alterar == "x":
            print("========================================================")        

    elif opcao == "X" or opcao == "x":
        break

    else:
        print("opção inválida")