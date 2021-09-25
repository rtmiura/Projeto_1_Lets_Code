# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:26:47 2021

@author: rodrigo
"""

#
import random
from unicodedata import normalize

# random.seed(0)

def sorteio_palavra(lista_palavras):    
    # print(conteudo_lista)
    palavra_secreta=random.choice(lista_palavras)
    
    while len(palavra_secreta)<=2:
        palavra_secreta=random.choice(lista_palavras)
        
    return palavra_secreta


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

    
def tratamento(palavra):    
    # print(conteudo_lista)
    palavra=palavra.upper().strip()
    palavra=remover_acentos(palavra)
    palavra=palavra.replace(' ','-')
    return palavra

def tratamento_letra(letra,Palavra_secreta):    
    if letra.upper()=='Ç':
        if not('Ç' in Palavra_secreta.upper()):
            return letra.upper().strip()
    else:
        return tratamento(letra)

def validade_letra_jogador(letra):
    if len(letra)>1:
        print(f'Você inseriu uma entrada invalida. {letra} tem mais de um caracter digitado--> ')
        return False
    if not letra.isalpha():
        print(f'Você inseriu uma entrada invalida. {letra} não é uma letra-> ')
        return False
    
    return True

def esconde_palavra(palavra):
    lista_nova_palavra=[]
    contador=0
    for letra in palavra:
        if letra.isalpha():
            lista_nova_palavra.append('*')
            contador+=1
        else:
            lista_nova_palavra.append(letra)
    nova_palavra=''.join(lista_nova_palavra)
    return nova_palavra, contador

def desenho_erros(tentativa):
    print("  ________    ")
    print(" |/      |    ")

    if(tentativa == 6):
        print(" |      (o)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 5):
        print(" |      (o)   ")
        print(" |       |     ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 4):
        print(" |      (o)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 3):
        print(" |      (o)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativa == 2):
        print(" |      (o)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativa == 1):
        print(" |      (o)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativa == 0):
        print(" |      (o)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print(" |__         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '.=========.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         .'   '.        ")
    print("        '-------'       ")
    
    
"""
Definição caracteristicas do jogo

"""
Numero_tentativas=7

"""
#Elemento 1 Leitura ou sorteio da palavra a ser descoberta:

"""

arquivo = open('Lista_Teste.txt', 'r', encoding="utf-8")
conteudo = arquivo.read()
    
arquivo.close()
conteudo_lista=conteudo.split('\n')


palavra_secreta=sorteio_palavra(conteudo_lista)
# palavra_secreta='abc'
# palavra_secreta='agua-viva'


"""
#Elemento 2 Tratamento da palavra secreta:

"""

Palavra_formatada=tratamento(palavra_secreta)
#Palavra='Água'

"""
#Elemento 3 esconder a palavra tratada para mostrar para o jogador:

"""

Palavra_Display,numero_letras=esconde_palavra(Palavra_formatada)

"""
#Elemento 4 print da palavra escondida para o jogador:

"""

print(f'Atenção! A palavra secreta tem {numero_letras} letras')




Letras_digitadas=[]


while Numero_tentativas>0:
    
    print(f'Palavra secreta: {Palavra_Display}',end='')
    
    """
    Elemento 5 leitura da tentativa do jogador:

    """
        
    Novaletra=input('Digite o teu palpite, uma letra da palavra secreta: ')
    if not validade_letra_jogador(Novaletra):
        continue
        
    Novaletra=tratamento_letra(Novaletra,palavra_secreta)
    
    """
    #Elemento 6 listando letras já digitadas:

    """

    if Novaletra in Letras_digitadas:
        print(f'A letra {Novaletra} já foi digitada!')
        if len(Letras_digitadas)>0:
            print(f'Você já digitou este conjunto de letras: {Letras_digitadas}')
        continue
    else:
        Letras_digitadas.append(Novaletra)
        
    
    """
    Elemento 7 Verificação se a palavra secreta contem a
    letra da tentativa do jogador

    """
    
    Vetor=[letra==Novaletra for letra in Palavra_formatada]
    
    
    """
    Elemento 8 Checar se o jogador acertou ou errou
    
    Elemento 9 Se acertou atualizar a palavra escondida com a letra
    Checar se jogador completou a palavra e ganhou    
    
    Elemento 10 Se errou incrementar o numero de erros
    Atualizar desenho da forca
    Checar se jogador perdeu
    
    """
    
    Palavra_Display_list=list(Palavra_Display)    


    if not True in Vetor: #jogador Errou
        Numero_tentativas-=1 #remove tentativa
        print(f'A palavra secreta não contém a letra {Novaletra}!')
        desenho_erros(Numero_tentativas) #desenha forca

        if Numero_tentativas<1: #checa se perdeu
            print(f'Perdeu a palavra era {palavra_secreta.upper()}!')
        else: #mostra o numero de tentaticas restantes
            print(f'Você pode cometer mais {Numero_tentativas} erros')
    
    else: #jogador Acertou
        print(f'A palavra secreta contém a letra {Novaletra}!')
        for i in range(len(Palavra_Display)): #Atualiza a letra na palavra escondida
            if Vetor[i]:
                Palavra_Display_list[i]=Novaletra
        Palavra_Display=''.join(Palavra_Display_list)
        
    
    
    if Palavra_Display==Palavra_formatada: #checa se ganhou
     print(f'Ganhou! A palavra secreta é {palavra_secreta.upper()}!')
     imprime_mensagem_vencedor()
     break
            
