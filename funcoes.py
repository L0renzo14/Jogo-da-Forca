import os

def limparTela():
    os.system("cls")

def jogar():
    letra=str(input("digite uma letra:"))
    return letra
   
def salvarDados(dados):
    arquivo = open("forca.txt","w")
    arquivo.writelines(dados)
    arquivo.close()

def lerDados():
    try:
        arquivo = open("forca.txt", "r")
    except:
        arquivo = open("forca.txt", "w")
        arquivo.close()
        arquivo = open("forca.txt", "r")
    dados = arquivo.readlines()
    arquivo.close()
    return dados    

def lerNomes(mensagemEntrada):
    valor = input(mensagemEntrada)
    return valor 


    