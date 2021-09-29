# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:39:29 2021

@author: Grupo 9 Lets Code
"""
#
import random
from unicodedata import normalize
import time

# random.seed(0)

def ler_lista_de_palavras(categoria_palavra):
    if categoria_palavra == "P":
        arquivo = open('lista_palavras_paises.txt', 'r', encoding="utf-8")
    elif categoria_palavra == "A":
        arquivo = open('lista_palavras_animais.txt', 'r', encoding="utf-8")
    elif categoria_palavra == "F":
        arquivo = open('lista_palavras_frutas.txt', 'r', encoding="utf-8")
    conteudo = arquivo.read()    
    arquivo.close()
    conteudo_lista=conteudo.split('\n')
    return conteudo_lista

def escolher_categoria_aleatoria():
    lista_categorias=["A","F","P"]
    categoria_palavra=random.choice(lista_categorias)
    return categoria_palavra

def print_categoria(categoria):
    print(f'A catergoria vai ser {categoria}')

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


def desenho_erros(tentativa,nome):
    print()
    time.sleep(0.5)
    print(f'Forca do {nome}')
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


def imprime_mensagem_vencedor(nome):
    time.sleep(0.5)
    print(f"\nParabéns {nome}, você ganhou!")
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

#################################################################################
class Jogador(object):
    def __init__(self,nome):
        self.name=nome
        self.vitorias=0
        self.derrotas=0
        self.n_tentativas_para_vencer=0
        
    def tenta_nova_letra(self):
        return input(f'{self.retorna_nome_jogador()} digite o teu palpite, uma letra da palavra secreta: ')
        
    def retorna_nome_jogador(self):
        return self.name
    
    def retorna_n_vitorias(self):
        return self.vitorias
    
    def retorna_n_derrotas(self):
        return self.derrotas
    
    def retorna_media_tentativas_para_ganhar(self):
        return self.n_tentativas_para_vencer/self.vitorias
    
    def atualiza_vitoria(self):
         self.vitorias+=1
         
    def atualiza_derrota(self):
         self.derrotas+=1
         
    def atualiza_n_tentativas_para_vencer(self,tentativas):
         self.n_tentativas_para_vencer+=tentativas
    
    
    def __str__(self):
        if self.vitorias>0:
            return (f'Nome: {self.name} - Vitórias: {self.vitorias} - Derrotas: {self.derrotas} - Média de tentativa para ganhar {self.n_tentativas_para_vencer/self.vitorias}')
        else:
            return (f'Nome: {self.name} - Vitórias: {self.vitorias} - Derrotas: {self.derrotas}')
    


class Forca(object):
    
    def __init__(self,conteudo_lista,Lista_Jogadores):
        
        self.Numero_tentativas=7
        
        self.palavra_secreta=sorteio_palavra(conteudo_lista)
        # self.palavra_secreta='abc'
        
        self.palavra_secreta_list=list(self.palavra_secreta)        
        self.Palavra_formatada=tratamento(self.palavra_secreta)
        
        self.Palavra_Comparar,self.numero_letras=esconde_palavra(self.Palavra_formatada)
        self.Palavra_Display=self.Palavra_Comparar
        

        
        self.Letras_digitadas=[]
        
        self.Lista_Jogadores=Lista_Jogadores
        random.shuffle(self.Lista_Jogadores)        
        self.Tentativas_Jogador={}
        
        self.Jogo_Valido=True
        self.Vencedor=[]
        self.Perdedores=[]
        
        print(f'Atenção! A palavra secreta tem {self.numero_letras} letras')
        for Jogador in Lista_Jogadores:
            self.Tentativas_Jogador[Jogador.retorna_nome_jogador()]=self.Numero_tentativas
            

    def numero_tentativas(self,Nome):
        return self.Tentativas_Jogador[Nome]
        
    def atualiza_fila(self):
        self.Lista_Jogadores.append(self.Lista_Jogadores.pop(0))
        
    def jogo_Valido(self):
        return self.Jogo_Valido
        
        

    def jogar(self):
        
        if len(self.Lista_Jogadores)<1:
           print('Sem Jogadores para jogar')
           self.Jogo_Valido=False
           return None
       
        Jogador_da_rodada=self.Lista_Jogadores[0]
        
        if self.numero_tentativas(Jogador_da_rodada.retorna_nome_jogador())>0:
            time.sleep(0.5)
            print(f'\nÉ a vez de {Jogador_da_rodada.retorna_nome_jogador()} jogar:')
            time.sleep(0.5)
            print(f'Palavra secreta: {self.Palavra_Display}',end='')
            time.sleep(0.5)
            self.Novaletra=Jogador_da_rodada.tenta_nova_letra()
            
            if not validade_letra_jogador(self.Novaletra):
                return None
            
            self.Novaletra=tratamento_letra(self.Novaletra,self.palavra_secreta)
            
            
            if self.Novaletra in self.Letras_digitadas:
                print(f'A letra {self.Novaletra} já foi digitada!')
                time.sleep(0.5)
                if len(self.Letras_digitadas)>0:
                    print(f'Já foi digitado este conjunto de letras: {self.Letras_digitadas}')
                    time.sleep(0.5)
                return None
            else:
                self.Letras_digitadas.append(self.Novaletra)
            
            
            Vetor=[letra==self.Novaletra for letra in self.Palavra_formatada]
            
            Palavra_Comparar_list=list(self.Palavra_Comparar)    
            Palavra_Display_list=list(self.Palavra_Display)
            
            if not True in Vetor: #jogador Errou
                self.Tentativas_Jogador[Jogador_da_rodada.retorna_nome_jogador()]-=1 #remove tentativa
                print(f'A palavra secreta não contém a letra {self.Novaletra}!')
                time.sleep(0.5)
                desenho_erros(self.Tentativas_Jogador[Jogador_da_rodada.retorna_nome_jogador()],Jogador_da_rodada.retorna_nome_jogador()) #desenha forca
                self.atualiza_fila()
                
                if self.Tentativas_Jogador[Jogador_da_rodada.retorna_nome_jogador()]<1: #checa se perdeu
                    print(f'{Jogador_da_rodada.retorna_nome_jogador()} perdeu !')
                    self.Perdedores.append(self.Lista_Jogadores.pop())
                    
                    if len(self.Lista_Jogadores)<1:
                        print('Sem Jogadores para jogar')
                        print(f'A palavra secreta era {self.palavra_secreta.upper()}')
                        self.Jogo_Valido=False
                        return None
                  
                else: #mostra o numero de tentaticas restantes
                    time.sleep(0.5)
                    print(f'{Jogador_da_rodada.retorna_nome_jogador()}, você pode cometer mais {self.Tentativas_Jogador[Jogador_da_rodada.retorna_nome_jogador()]} erros')
                
        
            else: #jogador Acertou
                time.sleep(0.5)
                print(f'A palavra secreta contém a letra {self.Novaletra}!')
                for i in range(len(self.Palavra_Comparar)): #Atualiza a letra na palavra escondida
                    if Vetor[i]:
                        Palavra_Comparar_list[i]=self.Novaletra
                        Palavra_Display_list[i]=self.palavra_secreta_list[i].upper()
                self.Palavra_Comparar=''.join(Palavra_Comparar_list)
                self.Palavra_Display=''.join(Palavra_Display_list)
                
                
            if self.Palavra_Comparar==self.Palavra_formatada: #checa se ganhou
                 time.sleep(0.5)
                 print(f'{Jogador_da_rodada.retorna_nome_jogador()} ganhou! A palavra secreta é {self.palavra_secreta.upper()}!')
                 imprime_mensagem_vencedor(Jogador_da_rodada.retorna_nome_jogador())
                 self.Vencedor.append(self.Lista_Jogadores.pop(0))
                 self.Jogo_Valido=False
                 if len(self.Lista_Jogadores)>0:
                     for i in range(len(self.Lista_Jogadores)):                        
                         self.Perdedores.append(self.Lista_Jogadores[i])
                     
                     
                
                    
        else:
            time.sleep(0.5)
            print(f'{Jogador_da_rodada.retorna_nome_jogador()} não tem mais tentativas')
            return None
            

# arquivo = open('lista_palavras_frutas.txt', 'r', encoding="utf-8")
# # arquivo = open('Lista_Teste.txt', 'r', encoding="utf-8")
# conteudo = arquivo.read()    
# arquivo.close()
# conteudo_lista=conteudo.split('\n')

dicionario_categorias={"A":"Animais","F":"Frutas", "P":"Países"}

print(f'O jogo tem 3 níveis de dificildade:\n *No nível fácil você escolhe a categoria da palavra \n *No nível médio o jogo escolhe a categoria para você e te avisa sobre a categoria escolhida \n *No nível difícil o jogo sorteia a palavra mas não te avisa sobre a categoria escolhida \n')
time.sleep(0.5)
dificuldade=input('Em qual dificuldade você quer jogar? Fácil(F), Médio(M) ou Díficil(D)')
dificuldade=dificuldade.upper()

while dificuldade not in ("F","M","D"):
    time.sleep(0.5)
    categoria_palavra=input('Em qual dificuldade você quer jogar? Fácil(F), Médio(M) ou Díficil(D)')  

if  dificuldade=="F":
    time.sleep(0.5)
    categoria_palavra=input('Qual categoria de palavras você quer? Países(P), Animais(A) ou Frutas(F)')
    categoria_palavra=categoria_palavra.upper()
    
    
    while categoria_palavra not in ("A","F","P"):
        time.sleep(0.5)
        categoria_palavra=input('Qual categoria de palavras você quer? Países(P), Animais(A) ou Frutas(F)')    

    print_categoria(dicionario_categorias[categoria_palavra])
    
elif dificuldade=="M":
        categoria_palavra=escolher_categoria_aleatoria()
        print_categoria(dicionario_categorias[categoria_palavra])
        
elif dificuldade=="D":
        categoria_palavra=escolher_categoria_aleatoria()



conteudo_lista=ler_lista_de_palavras(categoria_palavra)


Jogador1=Jogador('Ana Beatriz')

Jogador2=Jogador('Julia') 

# Jogador3=Jogador('Julia')

# Jogador4=Jogador('Rodrigo') 

lista_jogadores=[Jogador1,Jogador2]
 
Forca1=Forca(conteudo_lista,lista_jogadores)

Jogo_valido=True

while Jogo_valido:
    Forca1.jogar()
    Jogo_valido=Forca1.jogo_Valido()
