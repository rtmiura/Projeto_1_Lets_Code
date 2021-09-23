# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:26:47 2021

@author: rodrigo
"""


import random
from unicodedata import normalize

# Teste para github

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

"""
Definição caracteristicas do jogo
N erros
N Jogadores
etc
"""
Numero_tentativas=5

"""
#Elemento 1 Leitura ou sorteio da palavra a ser descoberta:

-Definição da palavra secreta
-Escolha por critério de dificuldade
-Verificar possiveis palavras sem sentido para jogo da forca

"""

arquivo = open('Palavras_red.txt', 'r', encoding="utf-8")
conteudo = arquivo.read()
    
arquivo.close()
conteudo_lista=conteudo.split('\n')


palavra_secreta=sorteio_palavra(conteudo_lista)
Palavra=tratamento(palavra_secreta)

#Palavra='Água'

"""
#Elemento 2 Tratamento da palavra secreta:

-Remover espaços antes e depois
-Colocar tudo num padrão, exemplo tudo maiusculo
- Definir como serão tratados acentos, traços no meio de palavras, 
letras diferentes como ç, etc

"""

Palavra_formatada=Palavra.strip().upper()

"""
#Elemento 3 esconder a palavra tratada para mostrar para o jogador:

"""

Palavra_Display=len(Palavra_formatada)*'*'


"""
#Elemento 4 print da palavra escondida para o jogador:

"""
print(Palavra_Display)


"""
#Elemento 6 listando letras já digitadas:

"""
Letras_digitadas=[]
while Numero_tentativas>0:
    """
    Elemento 5 leitura da tentativa do jogador:
        Jogador por tentar somente letra? pode tentar chutar a palavra direto?
        Ler letra
        Tratar letra, checar erros de digitação, ver se é uma letra de fato
        verificar se letra é repetida
        Dar feedbacks ao usuario

    """
    
    Novaletra=input('Digite Letra\n')
    
    if len(Novaletra)>1:
        print(f'Você provavelmente cometeu um erro. Foi digitado mais de um caracter --> {Novaletra}')
        continue
        
    Novaletra=Novaletra.strip().upper()
    

    if Novaletra in Letras_digitadas:
        print(f'A letra {Novaletra} já foi digitada!')
        print(Palavra_Display)
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


    if not True in Vetor:
        Numero_tentativas-=1
        print(f'A palavra secreta não contem a letra {Novaletra}!')
        if Numero_tentativas<1:
            print(f'Perdeu a palavra era {Palavra_formatada}!')
    else:        
        for i in range(len(Palavra_Display)):
            if Vetor[i]:
                Palavra_Display_list[i]=Novaletra
        Palavra_Display=''.join(Palavra_Display_list)
    print(Palavra_Display)
    
    
    if Palavra_Display==Palavra_formatada:
     print(f'Ganhou! A palavra secreta é {Palavra_Display}!')
     break
            

# print(' o ')
# print('/|\\')  
# print(' |')
# print('/ \\') 

# print('{:<5}'.format('-------'))
# print('{:<5}{}'.format('|',' |'))
# print('{:<5}{}'.format('|',' o'))
# print('{:<5}{}'.format('|','/|\\'))
# print('{:<5}{}'.format('|',' |'))
# print('{:<5}{}'.format('|','/ \\')) 
