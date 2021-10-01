# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:28:21 2021

@author: rodrigo
"""


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
    
class Jogador_Burro(Jogador):
    def __init__(self,nome):
        
        self.name=nome
        self.vitorias=0
        self.derrotas=0
        self.n_tentativas_para_vencer=0
        self.lista_Vogais=['A', 'I', 'O', 'E', 'U']
        self.lista_Consoantes=['R', 'N', 'C', 'L', 'T', 'M', 'S', 'B', 'G', 'D', 'P', 'H', 'V', 'J', 'F', 'K', 'Q', 'X', 'Z', 'W', 'Y']
        self.lista_letras_jogadas=[]
        
    def tenta_nova_letra(self,lista_letras_jogadas=[]):
        novas_letrar_para_tirar=[]
        
        for letra in lista_letras_jogadas:
            if letra not in self.lista_letras_jogadas:
                self.lista_letras_jogadas.append(letra)
                novas_letrar_para_tirar.append(letra)
            
        for letra in novas_letrar_para_tirar:
            if letra in self.lista_Vogais:
                self.lista_Vogais.remove(letra)
            if letra in self.lista_Consoantes:
                self.lista_Consoantes.remove(letra)
        
        if len(self.lista_Vogais)>0:
            letra_da_vez=self.lista_Vogais[0]
            self.lista_Vogais.remove(letra_da_vez)
            self.lista_letras_jogadas.append(letra_da_vez)            
            print(f'\nSou o robô {self.name}. Após calculos avançadosa letra certa é a vogal {letra_da_vez}')
            time.sleep(2)
            return letra_da_vez
        else:
            if len(self.lista_Consoantes)>0:
                letra_da_vez=self.lista_Consoantes[0]
                self.lista_Consoantes.remove(letra_da_vez)
                self.lista_letras_jogadas.append(letra_da_vez)
                print(f'\nSou o robô {self.name}. Após calculos avançados a letra certa é a consoante {letra_da_vez}')
                time.sleep(2)
                return letra_da_vez
            else:
                print(f'\nSou o robô {self.name}. Acabaram minhas letras')
                time.sleep(2)
    
    def reinicia_Robo(self):
         self.lista_Vogais=['A', 'I', 'O', 'E', 'U']
         self.lista_Consoantes=['R', 'N', 'C', 'L', 'T', 'M', 'S', 'B', 'G', 'D', 'P', 'H', 'V', 'J', 'F', 'K', 'Q', 'X', 'Z', 'W', 'Y']
         
        
    def atualiza_vitoria(self):
         self.vitorias+=1
         self.reinicia_Robo()
         
    def atualiza_derrota(self):
         self.derrotas+=1
         self.reinicia_Robo()
                    
                

Jair=Jogador_Burro('Jair')    

for i in range(26):  
    letra=Jair.tenta_nova_letra(['R','W','O','N'])

