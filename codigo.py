import random

def titulo():
    print('='*30)
    print("MANUAL DE RECEITAS")
    print('='*30)
    return

def funcao(opcao):
    if opcao == 'E' or opcao == 'e':
        funcionalidade_exibir = input("""                            
Como deseja ver as receitas?
[1] Tudo 
[2] Por país 
[3] Favoritos 
[4] Aleatório
""" )
        if funcionalidade_exibir == "1":
            file = open("tudo.txt", "r")
            print(file.read())
            return
        
        elif funcionalidade_exibir == "2":
            pais = input("digite o pais do qual deseja ver as receitas: ")
            
            file = open("tudo.txt", "r")
            
            for linha in file:
                if f"{pais};" in linha:
                    print(linha)
            return
        
        elif funcionalidade_exibir == "3":
            file = open("favoritos.txt", "r")
            print(file.read())
            file.close()
            return
        
        elif funcionalidade_exibir == "4":
            file = open("tudo.txt", "r")
            
            ret = []
            for linha in file:
                ret.append(linha)
                
            aleatorio = random.randint(0, len(ret)-1)
            
            print(ret[aleatorio])
            return
        
        else:
            print("Opção inválida.")
    
    elif opcao == 'A' or opcao == "a":
        funcionalidade_alterar = input("""
Como deseja deseja alterar uma receita?
[1] Adicionar 
[2] Remover 
[3] Editar 
""" )
        
        if funcionalidade_alterar == "1":
            pais = input("Digite o país de origem da nova receita: ")
            nome = input("Digite o nome da receita: ")
            preparo = input("Digite o preparo da receita com os ingredientes: ")
            novareceita = (f"{pais};{nome};{preparo}\n")
            
            file = open("tudo.txt", "a")
            file.write(novareceita)
            file.close()
            
            favoritos = input("""
deseja adicionar a receita aos favoritos?
[1] sim
[2] não
""")
            
            if favoritos == "1":
                file = open("favoritos.txt", "a")
                file.write(novareceita)
                file.close()    
            return
         
        elif  funcionalidade_alterar == "2":
            receita = input ("Digite o nome da receita que irá ser removida: ")
            
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
        
        elif funcionalidade_alterar == "3":
            receita = input("Digite a receita que irá ser editada: ")
            return receita

titulo()
while True:
    opcao = input("""
Exibir -------> E
Alterar ------> A                  

Digite a funcionalidade desejada: """)
    
    if opcao == "stop":
        break
    
    else:
        funcao(opcao)

