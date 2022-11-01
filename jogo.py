from funcoes import limparTela,lerDados,salvarDados,lerNomes

# Lorenzo Cornelio Pasqualotto RA:1132026

print("-="*15)
print("        JOGO DA FORCA")
print("-="*15)

desafiante=lerNomes("Nome Desafiante:")
competidor=lerNomes("Nome Competidor:")

dados = lerDados()
dados.append(("COMPETIDOR:"+competidor)+"\n"+("DESAFIANTE:"+desafiante+"\n"))
salvarDados(dados)

limparTela()
print('Nomes registrados com sucesso')

palavraChave=str(input('Palavra Chave:'))  
dica1=input('Dica1:')
dica2=input('Dica2:')
dica3=input('Dica3:')
dados = lerDados()
dados.append("PALAVRA CHAVE:"+palavraChave+"\n")
salvarDados(dados)

limparTela()

print("A palavra tem",len(palavraChave),"letras")
chances=5
digitadas=[]

while True:
    if chances == 5:
        jogar=int(input('Para Jogar, digite (1) ou Pedir Primeira Dica, digite (2)\n'))
        if jogar == 2:
            print("DICA 1:",dica1)
    elif chances == 3:
        jogar=int(input('Para Jogar digite (1) ou Pedir Segunda Dica digite (2)\n'))
        if jogar == 2:
            print("DICA 2:",dica2)          
    elif chances == 1:
        jogar=int(input('Para Jogar ,digite (1) ou Pedir Terceira Dica ,digite (2)\n'))
        if jogar ==2:
            print("DICA 3:",dica3)       
        continue
    letra = str(input('Digite uma letra:'))
    if len(letra)>1:
        print("Erro não pode mais de uma letra")
        continue  
    digitadas.append(letra)
    palavra_secreta=''
    
    for letra_secrerta in palavraChave:
        if letra_secrerta in digitadas:
            palavra_secreta += letra_secrerta
        else:
            palavra_secreta += "\033[31m*\033[m"
    if palavra_secreta == palavraChave:
        print('\033[1;32mVoce venceu e escapou da forca\033[m')
        dados= lerDados()
        dados.append("PARABENS,"+competidor+",VOCE VENCEU"+"\n")
        salvarDados(dados)
        break
    else:
        print("A palavra secreta está assim:",palavra_secreta)
    
    if letra not in palavraChave:
            chances-= 1    
    elif chances <=0:
        print("Voce PERDEU!","\n",desafiante,"VOCE VENCEU")
        dados= lerDados()
        dados.append("PARABENS,"+desafiante+",VOCE VENCEU"+"\n")
        salvarDados(dados)
        break
    print("Voce tem",chances,"chances.")  

   