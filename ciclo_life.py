import time
import random
import threading
from incoterm import IncotermTransaction, flags_siscomex


class CicloLifeSiscomex(threading.Thread):
    def __init__(self, transaction: IncotermTransaction, tempo_min=1, tempo_max=30):
        super().__init__()
        self.transaction = transaction
        self.tempo_min = tempo_min
        self.tempo_max = tempo_max

    def run(self):
        # pega a flag final negociada da transação
        flag_final = self.transaction.flag_negociada()
        print(f"\n🚢 Iniciando ciclo da transação {self.transaction.id_incoterm}")
        print(f"Transação completa: {self.transaction.definido_comex()}")
        print(f"Flag final negociada: {flag_final}\n")

        # percorre as flags na ordem até chegar na flag escolhida
        for flag in flags_siscomex:
            tempo = random.randint(self.tempo_min, self.tempo_max)
            time.sleep(tempo)
            print(f"[{self.transaction.id_incoterm}] ➡️ Atualização: Flag = {flag} (após {tempo}horas)")
            if flag == flag_final:
                print(f"[{self.transaction.id_incoterm}] ✅ Ciclo concluído na flag: {flag_final}\n")
                break


if __name__ == "__main__":
    # cria várias transações simultâneas
    transacoes = [IncotermTransaction(50000, 3000) for _ in range(3)]

    # cria threads para cada ciclo
    ciclos = [CicloLifeSiscomex(t) for t in transacoes]

    # inicia todas as threads
    for ciclo in ciclos:
        ciclo.start()

    # aguarda todas terminarem
    for ciclo in ciclos:
        ciclo.join()
