import csv

def calcula_pontuacao(palavra_secreta, tentativas_jogador):
    pontuacao = len(palavra_secreta) * tentativas_jogador
    return pontuacao

#pontuacao=pontuacao_ranking(5,"abelha")
#print(pontuacao)

def abrir_rank():   
    arquivo = open('ranking.csv', 'r', encoding = "utf-8")
    read_csv = csv.reader(arquivo, delimiter=',', lineterminator='\n')

    ranking = {}
    for line in read_csv:
        nome_jogador_rank = line[0]
        pontuacao_jogador_rank = int(line[1])
        ranking[nome_jogador_rank] = pontuacao_jogador_rank
    arquivo.close()
    return ranking

def atualiza_rank(nome_jogador,pontuacao):
    ranking_atualizado = abrir_rank()

    ranking_atualizado[nome_jogador] = pontuacao

    arquivo = open('ranking.csv', 'w', encoding = "utf-8")
    write_csv = csv.reader(arquivo, delimiter =',', lineterminator = '\n').writerows(ranking_atualizado)
    write_csv.close()

    return ranking_atualizado

def ordena_rank(ranking):
    ranking.sort(key=lambda item : item[1])
    ranking_final = ranking
    return ranking_final
