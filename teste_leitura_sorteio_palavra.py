# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:43:54 2021

@author: rodrigo
"""

import random
from unicodedata import normalize

# if __name__ == '__main__':
#     from doctest import testmod
#     testmod()

arquivo = open('Palavras_red.txt', 'r', encoding="utf-8")
conteudo = arquivo.read()
    
arquivo.close()
conteudo_lista=conteudo.split('\n')

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


palavra_secreta=sorteio_palavra(conteudo_lista)
teste=tratamento(palavra_secreta)

