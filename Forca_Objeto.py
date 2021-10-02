# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:39:29 2021

@author: Grupo 9 Lets Code
"""
#
import random
from unicodedata import normalize
import time
import csv
random.seed(0)



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

def Numero_Jogadores():

    N=input(f'{Colors.BOLD}Quantos jogadores irão jogar nesta rodada?  ')
    
    try:
        Numero=int(N)
        if Numero<1:
            raise Exception('Numero de Jogadores Menor que 1')
        elif Numero>5:
            raise Exception('Numero de Jogadores Maior que 5')
        return Numero        
    except Exception as error:
        print(error)
        return Numero_Jogadores()


def desenho_erros(tentativa,nome):
    print()
    time.sleep(1.0)
    print(f'Forca de {nome}')
    print("  ________    ")
    print(" |/      |    ")

    if(tentativa == 4):
        print(" |      (o)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if(tentativa == 3):
        print(" |      (o)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |      /     ")

    if(tentativa == 2):
        print(" |      (o)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |      / \   ")

    if(tentativa == 1):
        print(" |      (o)   ")
        print(" |      \|    ")
        print(" |       |    ")
        print(" |      / \   ")

    if (tentativa == 0):
        print(" |      (o)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print(" |__         ")
    print()


def imprime_mensagem_vencedor(nome):
    time.sleep(1.0)
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
    print()

#################################################################################
class Jogador(object):
    def __init__(self,nome):
        self.name=nome
        self.vitorias=0
        self.derrotas=0
        self.pontos=0
        self.n_tentativas_para_vencer=0
        
    def tenta_nova_letra(self):
        return input(f'{self.retorna_nome_jogador()} digite o teu palpite, uma letra da palavra secreta: ')
        
    def retorna_nome_jogador(self):
        return self.name
    
    def retorna_n_vitorias(self):
        return self.vitorias
    
    def retorna_n_derrotas(self):
        return self.derrotas
    
    def retorna_pontos(self):
        return self.pontos
    
    
    def retorna_media_tentativas_para_ganhar(self):
        return self.n_tentativas_para_vencer/self.vitorias
    
    def atualiza_vitoria(self,pontuacao):
         self.vitorias+=1
         self.pontos+=pontuacao
         
    def atualiza_derrota(self):
         self.derrotas+=1
         
    def atualiza_n_tentativas_para_vencer(self,tentativas):
         self.n_tentativas_para_vencer+=tentativas
    
    
    def __str__(self):
        if self.vitorias>0:
            return (f'Nome: {self.name} - Vitórias: {self.vitorias} - Derrotas: {self.derrotas}')
        else:
            return (f'Nome: {self.name} - Vitórias: {self.vitorias} - Derrotas: {self.derrotas}')
    
class Jogador_Burro(Jogador):
    def __init__(self,nome):
        
        self.name=nome
        self.vitorias=0
        self.derrotas=0
        self.pontos=0
        self.lista_Vogais=['A', 'I', 'O', 'E', 'U']
        self.lista_Consoantes=['R', 'N', 'C', 'L', 'T', 'M', 'S', 'B', 'G', 'D', 'P', 'H', 'V', 'J', 'F', 'K', 'Q', 'X', 'Z', 'W', 'Y']
        self.lista_letras_jogadas=[]
        
    def tenta_nova_letra(self,lista_letras_jogadas=[]):

        
        for letra in lista_letras_jogadas:
            if letra not in self.lista_letras_jogadas:
                self.lista_letras_jogadas.append(letra)

            
        for letra in lista_letras_jogadas:
            if letra in self.lista_Vogais:
                self.lista_Vogais.remove(letra)
            if letra in self.lista_Consoantes:
                self.lista_Consoantes.remove(letra)
        
        if len(self.lista_Vogais)>0:
            letra_da_vez=self.lista_Vogais[0]
            self.lista_Vogais.remove(letra_da_vez)
            self.lista_letras_jogadas.append(letra_da_vez)            
            print(f'\nSou o robô {self.name}. Após cálculos avançados a letra certa é a vogal {letra_da_vez}')
            time.sleep(3)
            return letra_da_vez
        else:
            if len(self.lista_Consoantes)>0:
                letra_da_vez=self.lista_Consoantes[0]
                self.lista_Consoantes.remove(letra_da_vez)
                self.lista_letras_jogadas.append(letra_da_vez)
                print(f'\nRobô {self.name}: \"Após cálculos avançados a letra certa é a consoante {letra_da_vez}\"')
                time.sleep(3)
                return letra_da_vez
            else:
                print(f'\nSou o robô {self.name}. Acabaram minhas letras')
                time.sleep(3)
    
    def reinicia_Robo(self):
         self.lista_Vogais=['A', 'I', 'O', 'E', 'U']
         self.lista_Consoantes=['R', 'N', 'C', 'L', 'T', 'M', 'S', 'B', 'G', 'D', 'P', 'H', 'V', 'J', 'F', 'K', 'Q', 'X', 'Z', 'W', 'Y']
         
        
    def atualiza_vitoria(self,pontuacao):
         self.vitorias+=1
         self.pontos+=pontuacao
         self.reinicia_Robo()
         
    def atualiza_derrota(self):
         self.derrotas+=1
         self.reinicia_Robo()

class Forca(object):
    
    def __init__(self,Lista_Jogadores):
        
        comeco_jogo = ['Só dará errado se você tentar',
               'Seja forte, desista antes de começar!',
               'O caminho é longo, mas a derrota é certa!']
       
        
        self.Numero_tentativas=5

        ###############################################################################    
        dicionario_categorias={"A":"Animais","F":"Frutas", "P":"Países"}

        print(f'\nO jogo tem 3 níveis de dificildade:\n *No nível fácil você escolhe a categoria da palavra \n\n *No nível médio o jogo escolhe a categoria para você e\n te avisa sobre a categoria escolhida \n\n *No nível difícil o jogo sorteia a palavra mas\n não te avisa sobre a categoria escolhida \n')
        time.sleep(1)
        dificuldade=input('Em qual dificuldade você quer jogar? Fácil(F), Médio(M) ou Díficil(D) ')
        self.dificuldade=dificuldade.upper().strip()
        
        while self.dificuldade not in ("F","M","D"):
            time.sleep(1.0)
            dificuldade=input('Em qual dificuldade você quer jogar? Fácil(F), Médio(M) ou Díficil(D) ')  
            self.dificuldade=dificuldade.upper().strip()

        if  self.dificuldade=="F":
            time.sleep(1.0)
            categoria_palavra=input('Qual categoria de palavras você quer? Países(P), Animais(A) ou Frutas(F) ')
            categoria_palavra=categoria_palavra.upper().strip()
            
            
            while categoria_palavra not in ("A","F","P"):
                time.sleep(1.0)
                categoria_palavra=input('Qual categoria de palavras você quer? Países(P), Animais(A) ou Frutas(F) ') 
                categoria_palavra=categoria_palavra.upper().strip()   
        
            print_categoria(dicionario_categorias[categoria_palavra])
            self.categoria_palavra=dicionario_categorias[categoria_palavra]

        elif self.dificuldade=="M":
                categoria_palavra=escolher_categoria_aleatoria()
                print_categoria(dicionario_categorias[categoria_palavra])
                self.categoria_palavra=dicionario_categorias[categoria_palavra]

        elif self.dificuldade=="D":
                categoria_palavra=escolher_categoria_aleatoria()
                self.categoria_palavra=''
        
        
        
        conteudo_lista=ler_lista_de_palavras(categoria_palavra)
    
        ##############################################################################    
        
        self.palavra_secreta=sorteio_palavra(conteudo_lista)
        #self.palavra_secreta='aizv'
        
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
        
        
        print('\n'+random.choice(comeco_jogo)+'\n')
        time.sleep(1.0)
        
        if len(self.Lista_Jogadores)>1:
            print('Os Jogadores vão jogar na seguinte ordem:')
            for i in range(len(self.Lista_Jogadores)):
                print(f'P{i+1} - {self.Lista_Jogadores[i].retorna_nome_jogador()}')
            print()
            time.sleep(1.0) 

        
        print(f'Atenção! A palavra secreta tem {self.numero_letras} letras')
        time.sleep(0.5)
        
        for Jogador in Lista_Jogadores:
            self.Tentativas_Jogador[Jogador.retorna_nome_jogador()]=self.Numero_tentativas
            

    def numero_tentativas(self,Nome):
        return self.Tentativas_Jogador[Nome]
        
    def atualiza_fila(self):
        self.Lista_Jogadores.append(self.Lista_Jogadores.pop(0))
        
    def jogo_Valido(self):
        return self.Jogo_Valido
        
    def calcula_pontuacao(self, Jogador):
        pontuacao = len(self.palavra_secreta) * self.Tentativas_Jogador[Jogador.retorna_nome_jogador()]
        return pontuacao 

    def jogar(self):
        
        errou_letra = ['quando sua mente pensar em desistir, nem pense: desista',
               'lute como nunca, perca como sempre',
               'você já ta perdendo, agora é a humilhação',
               'seja protagonista do seu fracasso, você errou mais uma vez!',
               'nunca é tarde para começar a desistir!',
               'planeje os erros do futuro',
               'seja forte, desista',
               'cara, você com certeza é estúpido',
               'sério?! Meteu essa mané?',
               'que chute foi esse? É de cair o ** da b*nd*!',
               'papo reto... Melhor desistir']
        
        perdeu_geral = ['Se até um pé-na-bunda te dá aquele empurrão na vida, porque desanimar com as tragédias que acontecem conosco?',
                'Não se conforme com a derrota de hoje, amanhã tem mais',
                'Não sabendo que era impossível foi lá e SOUBE!',
                'Seu único limite é você mesmo, kkkkk',
                'Palmeiras não tem mundial!',
                'Simplesmente o Ibis do Jogo de Forca']
        
        msg_acertou_letra=['o Pelé',
                       'o Chuck Norris',
                       'o Rocky Balboa',
                       'o Pudim na Airfryer',
                       'o Michal Jordan',
                       'o Eistein',
                       'o Messi',
                       'a Angela Merkel',
                       'a Rebeca Andrade',
                       'a Marta',
                       'o pão na chapa',
                       'o Naruto',
                       'a cervejinha gelada na praia',
                       ]
        
        if len(self.Lista_Jogadores)<1:
           print('Sem Jogadores para jogar')
           self.Jogo_Valido=False
           return None
       
        Jogador_da_rodada=self.Lista_Jogadores[0]
        
        if self.numero_tentativas(Jogador_da_rodada.retorna_nome_jogador())>0:
            time.sleep(1.0)
            print(f'\nÉ a vez de {Jogador_da_rodada.retorna_nome_jogador()} jogar:')
            time.sleep(1.0)
            if self.dificuldade != 'D':
                print(f'Palavra secreta: {self.Palavra_Display}\nCategoria: {self.categoria_palavra}')
            else:
                 print(f'Palavra secreta: {self.Palavra_Display}')
            time.sleep(1.0)
            
            if type(Jogador_da_rodada).__name__=='Jogador':
                self.Novaletra=Jogador_da_rodada.tenta_nova_letra()
                
            elif type(Jogador_da_rodada).__name__=='Jogador_Burro':
                self.Novaletra=Jogador_da_rodada.tenta_nova_letra(self.Letras_digitadas)
            
            if not validade_letra_jogador(self.Novaletra):
                return None
            
            self.Novaletra=tratamento_letra(self.Novaletra,self.palavra_secreta)
            
            
            if self.Novaletra in self.Letras_digitadas:
                print(f'A letra {self.Novaletra} já foi digitada!')
                time.sleep(1.0)
                if len(self.Letras_digitadas)>0:
                    print(f'Já foi digitado este conjunto de letras: {self.Letras_digitadas}')
                    time.sleep(1.0)
                return None
            else:
                self.Letras_digitadas.append(self.Novaletra)
            
            
            Vetor=[letra==self.Novaletra for letra in self.Palavra_formatada]
            
            Palavra_Comparar_list=list(self.Palavra_Comparar)    
            Palavra_Display_list=list(self.Palavra_Display)
            
            if not True in Vetor: #jogador Errou
                self.Tentativas_Jogador[Jogador_da_rodada.retorna_nome_jogador()]-=1 #remove tentativa
                
                print(f'A palavra não contém {self.Novaletra}!')
                time.sleep(0.5)
                print(f'\n{Jogador_da_rodada.retorna_nome_jogador()} '+random.choice(errou_letra)+'\n')
                
                time.sleep(1.0)
                desenho_erros(self.Tentativas_Jogador[Jogador_da_rodada.retorna_nome_jogador()],Jogador_da_rodada.retorna_nome_jogador()) #desenha forca
                self.atualiza_fila()
                
                if self.Tentativas_Jogador[Jogador_da_rodada.retorna_nome_jogador()]<1: #checa se perdeu
                    print(f'{Jogador_da_rodada.retorna_nome_jogador()} perdeu !')
                    time.sleep(1.0)
                    print('\n'+random.choice(perdeu_geral)+'\n')
                    time.sleep(1.0)
                    Jogador_da_rodada.atualiza_derrota()
                    self.Perdedores.append(self.Lista_Jogadores.pop())
                    
                    if len(self.Lista_Jogadores)<1:
                        print('Sem Jogadores para jogar')
                        print(f'A palavra secreta era {self.palavra_secreta.upper()}')
                        self.Jogo_Valido=False
                        return None
                  
                else: #mostra o numero de tentaticas restantes
                    time.sleep(1.0)
                    print(f'{Jogador_da_rodada.retorna_nome_jogador()}, você pode cometer mais {self.Tentativas_Jogador[Jogador_da_rodada.retorna_nome_jogador()]} erros')
                
        
            else: #jogador Acertou
                time.sleep(1.0)
                print(f'A palavra secreta contém a letra {self.Novaletra}!')
                print(f'\n{Jogador_da_rodada.retorna_nome_jogador()} é simplesmente '+random.choice(msg_acertou_letra)+' do jogo de forca')
                for i in range(len(self.Palavra_Comparar)): #Atualiza a letra na palavra escondida
                    if Vetor[i]:
                        Palavra_Comparar_list[i]=self.Novaletra
                        Palavra_Display_list[i]=self.palavra_secreta_list[i].upper()
                self.Palavra_Comparar=''.join(Palavra_Comparar_list)
                self.Palavra_Display=''.join(Palavra_Display_list)
                
                
            if self.Palavra_Comparar==self.Palavra_formatada: #checa se ganhou
                 time.sleep(1.0)
                 print(f'{Jogador_da_rodada.retorna_nome_jogador()} ganhou! A palavra secreta é {self.palavra_secreta.upper()}!')
                 imprime_mensagem_vencedor(Jogador_da_rodada.retorna_nome_jogador())
                 Pontuacao=self.calcula_pontuacao(Jogador_da_rodada)
                 
                 Jogador_da_rodada.atualiza_vitoria(Pontuacao)
                 self.Vencedor.append(self.Lista_Jogadores.pop(0))
                 self.Jogo_Valido=False
                 if len(self.Lista_Jogadores)>0:
                     for i in range(len(self.Lista_Jogadores)):
                        print(f'{self.Lista_Jogadores[i].retorna_nome_jogador()} perdeu !') 
                        time.sleep(1.0)
                        print('\n'+random.choice(perdeu_geral)+'\n')
                        time.sleep(1.0)
                        self.Lista_Jogadores[i].atualiza_derrota()
                        self.Perdedores.append(self.Lista_Jogadores[i])
                     
                     
                
                    
        else:
            time.sleep(1.0)
            print(f'{Jogador_da_rodada.retorna_nome_jogador()} não tem mais tentativas')
            return None
            

class Colors(object):
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m' 
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[;7m"           

###################################################################################



# dic_jogadores={'Ana Beatriz':Jogador('Ana Beatriz'),
#                'Julia':Jogador('Julia'),
#                'Camila':Jogador('Camila'),
#                'Rodrigo':Jogador('Rodrigo'),
#                'Brian':Jogador('Brian'),
#                'Paty':Jogador('Paty'),
#                'Robo 1':Jogador_Burro('Robo Lento'),
#                'Robo 2':Jogador_Burro('Robo mais lento')               
#                }

dic_jogadores={}

Restart_jogo=False


while not Restart_jogo:

    
    

    lista_jogadores_rodada=[]
    print(f'\n {Colors.RED} ****SEJA BEM VINDO AO JOGO DE FORCA DA LETS CODE**** {Colors.RESET} \n')

    nome_jogadores_rodada=[]
    
    N_jogadores=Numero_Jogadores()
    
    for n_player in range(N_jogadores):
        Nome_jogador=input(f'\nEscreva o nome de um jogador que irá jogar rodada:{Colors.RESET} ')        
        
        if Nome_jogador in nome_jogadores_rodada:
            jogador_valid=False
            while not jogador_valid:
                print('Este Jogador já foi cadastrado')
                Nome_jogador=input('Escreva o nome de um jogador diferente: ')
                if Nome_jogador not in nome_jogadores_rodada:
                     jogador_valid=True
            
        
        if Nome_jogador not in dic_jogadores:
            Tipo_jogador=input('Tipo de Jogador: Humano = 1 / Robô !=1 -')
            if Tipo_jogador=='1':
                dic_jogadores[Nome_jogador]=Jogador(Nome_jogador)
            else:
                 dic_jogadores[Nome_jogador]=Jogador_Burro(Nome_jogador)
        
        nome_jogadores_rodada.append(Nome_jogador)
        lista_jogadores_rodada.append(dic_jogadores[Nome_jogador])       

     

    
    
    Jogo_valido=True
    
   
    Forca1=Forca(lista_jogadores_rodada)
    
    while Jogo_valido:
        Forca1.jogar()
        Jogo_valido=Forca1.jogo_Valido()
    
    Restart_jogo = input(f'{Colors.BOLD}Quer continuar a jogar? Sim = 1, Não = 0 ') != '1'







#############################################################################
print()

for jogador in dic_jogadores.values():
    print(jogador)

def vitorias_jogador(dicionario,jogador):
    return dicionario[jogador].retorna_n_vitorias()

def percentual_vitorias_jogador(dicionario,jogador):
    if dicionario[jogador].retorna_n_vitorias()>0 or dicionario[jogador].retorna_n_derrotas()>0:
        return (dicionario[jogador].retorna_n_vitorias())/(dicionario[jogador].retorna_n_derrotas()+dicionario[jogador].retorna_n_vitorias())
    else:
        return 0

Ranking_Jogadores_Vitorias=[jogador for jogador in dic_jogadores]
Ranking_Jogadores_Aproveitamento=[jogador for jogador in dic_jogadores]

Ranking_Jogadores_Vitorias.sort(key=lambda x:vitorias_jogador(dic_jogadores,x),reverse=True)
Ranking_Jogadores_Aproveitamento.sort(key=lambda x:percentual_vitorias_jogador(dic_jogadores,x),reverse=True)


print()
print('Ranking Por Número de Vitórias:')
for i in range(len(Ranking_Jogadores_Vitorias)):
    print(f'N° {i+1:2.0f} - Jogador: {Ranking_Jogadores_Vitorias[i]:12s} - Vitórias {vitorias_jogador(dic_jogadores,Ranking_Jogadores_Vitorias[i]):4.1f}')

print()
print('Ranking percentual de vitórias:')
for i in range(len(Ranking_Jogadores_Aproveitamento)):
    print(f'N° {i+1:2.0f} - Jogador: {Ranking_Jogadores_Vitorias[i]:12s} - Aproveitamento {100*percentual_vitorias_jogador(dic_jogadores,Ranking_Jogadores_Vitorias[i]):4.1f} %')


# def abrir_rank():   
#     arquivo = open('ranking.csv', 'r', encoding = "utf-8")
#     read_csv = csv.reader(arquivo, delimiter=',', lineterminator='\n')

#     ranking = {}
#     for line in read_csv:
#         nome_jogador_rank = line[0]
#         vitorias_jogador_rank = int(line[1])
#         pontuacao_jogador_rank = int(line[2])
#         ranking[nome_jogador_rank] = [vitorias_jogador_rank, pontuacao_jogador_rank]
#     arquivo.close()
#     return ranking   
 
# def atualiza_rank(ranking,dic_jogadores):

#     for jogador in dic_jogadores:
#         if jogador in ranking:
#             ranking[jogador][0] += dic_jogadores[jogador].retorna_n_vitorias()
#             ranking[jogador][1] += dic_jogadores[jogador].retorna_pontos()
#         else:
#             ranking[jogador][0] = dic_jogadores[jogador].retorna_n_vitorias()
#             ranking[jogador][1] = dic_jogadores[jogador].retorna_pontos()
            

    
#     arquivo = open('ranking.csv', 'w', encoding = "utf-8")
#     write_csv = csv.reader(arquivo, delimiter =',', lineterminator = '\n').writerows(ranking_atualizado)
#     write_csv.close()

#     return ranking_atualizado