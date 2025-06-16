import random
import time

class AviatorBot:
    def __init__(self, banca_inicial, porcentagem_aposta, multiplicador_sair):
        self.banca = banca_inicial
        self.porcentagem_aposta = porcentagem_aposta
        self.multiplicador_sair = multiplicador_sair
        self.historico = []

    def apostar(self):
        # Valor da aposta é % da banca atual
        aposta = self.banca * self.porcentagem_aposta
        return round(aposta, 2)

    def resultado_rodada(self):
        # Simula multiplicador do Aviator (aleatório entre 1.0 e 10.0)
        return round(random.uniform(1.0, 10.0), 2)

    def estrategia(self, multiplicador):
        # Sai da aposta se multiplicador atingir ou passar o limite definido
        return multiplicador >= self.multiplicador_sair

    def jogar(self, rodadas):
        for i in range(rodadas):
            if self.banca <= 0:
                print("Banca zerada. Fim do jogo.")
                break
            
            aposta = self.apostar()
            multiplicador = self.resultado_rodada()
            ganhou = self.estrategia(multiplicador)

            if ganhou:
                ganho = aposta * (multiplicador - 1)
                self.banca += ganho
                self.historico.append(('Ganho', multiplicador, ganho, self.banca))
                print(f"Rodada {i+1}: Saiu no {multiplicador}x, ganhou R${ganho:.2f}. Banca: R${self.banca:.2f}")
            else:
                self.banca -= aposta
                self.historico.append(('Perda', multiplicador, -aposta, self.banca))
                print(f"Rodada {i+1}: Saiu no {multiplicador}x, perdeu R${aposta:.2f}. Banca: R${self.banca:.2f}")

            time.sleep(0.5)  # Pausa para simular tempo real

        print("\nResumo final:")
        ganhos = sum(x[2] for x in self.historico if x[2] > 0)
        perdas = -sum(x[2] for x in self.historico if x[2] < 0)
        print(f"Total ganho: R${ganhos:.2f}")
        print(f"Total perdido: R${perdas:.2f}")
        print(f"Banca final: R${self.banca:.2f}")

if __name__ == "__main__":
    banca_inicial = 100.0           # R$ 100,00 de banca inicial
    porcentagem_aposta = 0.05       # Aposta 5% da banca em cada rodada
    multiplicador_sair = 2.0        # Sai do jogo quando atingir 2x multiplicador
    rodadas = 30                    # Número de rodadas para simular

    bot = AviatorBot(banca_inicial, porcentagem_aposta, multiplicador_sair)
    bot.jogar(rodadas)
