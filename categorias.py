import random

dicionario_categorias={"A":"Animais","F":"Frutas", "P":"Países"}

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
    
    


Nome_jogador=input('Escreva o Nome do jogador da rodada: ') 

print(f'O jogo tem 3 níveis de dificildade:\n *No nível fácil você escolhe a categoria da palavra \n *No nível médio o jogo escolhe a categoria para você e te avisa sobre a categoria escolhida \n *No nível difícil o jogo sorteia a palavra mas não te avisa sobre a categoria escolhida \n')
dificuldade=input('Em qual dificuldade você quer jogar? Fácil(F), Médio(M) ou Díficil(D)')
dificuldade=dificuldade.upper()

while dificuldade not in ("F","M","D"):
    categoria_palavra=input('Em qual dificuldade você quer jogar? Fácil(F), Médio(M) ou Díficil(D)')  

if  dificuldade=="F":  
    categoria_palavra=input('Qual categoria de palavras você quer? Países(P), Animais(A) ou Frutas(F)')
    categoria_palavra=categoria_palavra.upper()
    
    
    while categoria_palavra not in ("A","F","P"):
        categoria_palavra=input('Qual categoria de palavras você quer? Países(P), Animais(A) ou Frutas(F)')    

    print_categoria(dicionario_categorias[categoria_palavra])
    
elif dificuldade=="M":
        categoria_palavra=escolher_categoria_aleatoria()
        print_categoria(dicionario_categorias[categoria_palavra])
        
elif dificuldade=="D":
        categoria_palavra=escolher_categoria_aleatoria()



conteudo_lista=ler_lista_de_palavras(categoria_palavra)



