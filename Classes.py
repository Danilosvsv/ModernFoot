import random
import datetime
import time

class jogador:
    def __init__(self, nome, aniversario, idade, altura, valor, posicao, qualidade, salario, condicionamento, caracteristicas):
        self.nome = nome
        self.aniversario = aniversario
        self.idade = idade
        self.altura = altura
        self.valor = valor
        self.posicao = posicao
        self.qualidade = qualidade
        self.salario = salario
        self.condicionamento = condicionamento
        self.caracteristicas = caracteristicas

class clube:
    def __init__(self, nome, liga, pais, patrimonio, qualidade, relevancia):
        self.nome = nome
        self.liga = liga
        self.pais = pais
        self.patrimonio = patrimonio
        self.qualidade = qualidade
        self.relevancia = relevancia
        self.jogadores = []
        self.treinador = []
        
class estadio: 
    def __init__(self, nome, clube, capacidade):
        self.nome = nome 
        self.clube = clube
        self.capacidade = capacidade    

class treinador:
    def __init__(self, nome, nacionalidade, tatica, qualidade):
        self.nome = nome 
        self.nacionalidade = nacionalidade    
        self.tatica = tatica    
        self.qualidade = qualidade 

class liga:
    def __init__(self, nome, pais, qualidade, divisao, tipo):
        self.nome = nome
        self.liga = liga
        self.pais = pais
        self.qualidade = qualidade
        self.clubes = []

class financas:

    def __init__(self, saldo, receita, despesa, divida):
        self.saldo = saldo
        self.receita = receita
        self.despesa = despesa
        self.divida = divida

        def fRecebeEmprestimo(self, valor_emprestimo):
            self.saldo += valor_emprestimo
            if 0 < valor_emprestimo <= 5000000:
                self.divida = 0.035*valor_emprestimo
            elif 5000000.01 <= valor_emprestimo <= 10000000:
                self.divida = 0.065*valor_emprestimo
            else: 
                self.divida = 0.125*valor_emprestimo

        def fPagaEmprestimo(self, valor):
            if valor > 0 and valor <= self.saldo and valor <= self.divida:
                self.saldo -= valor
                self.divida -= valor

class jogos:
    def __init__(self, mandante, visitante, publico, renda, posse_mandante, posse_visitante, finalizacoes_mandante, finalizacoes_visitante, desarmes_mandante, desarmes_visitante, passes_mandante, passes_visitante):
        self.mandante = mandante
        self.visitante = visitante
        self.publico = publico
        self.renda = renda
        self.posse_mandante = posse_mandante
        self.posse_visitante = posse_visitante
        self.finalizacoes_mandante = finalizacoes_mandante
        self.finalizacoes_visitante = finalizacoes_visitante
        self.desarmes_mandante = desarmes_mandante
        self.desarmes_visitante = desarmes_visitante
        self.passes_mandante = passes_mandante
        self.passes_visitante = passes_visitante

class calendario:
    def __init__(self):
        self.mes_atual = 1
        self.ano_atual = 2024
        self.jogos_agendados = {}

    def agendar_jogo(self, time_a, time_b):
        chave = f"{datetime.date(2024, 1, 1).strftime('%d/%m/%Y')}"
        self.jogos_agendados[chave] = (time_a, time_b)

    def avancar_mes(self):
        self.mes_atual += 1
        if self.mes_atual > 12:
            self.mes_atual = 1
            self.ano_atual += 1

     
#if __name__ == "__main__":
    #main()