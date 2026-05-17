import random
import uuid   # para gerar id único

flags_siscomex = ['incon', 'embar', 'modal', 'desem', 'libera']
paises = ['Brasil', 'Estados Unidos', 'Italia', 'França', 'China', 'Argentina']
importadores = ['NA Importador', 'NB Importador', 'NC Importador']
exportadores = ['GA Exportador', 'GB Exportador', 'GC Exportador']
produtos = ['arroz', 'feijão', 'soja', 'frutas', 'eletrônico', 'minério']


class IncotermTransaction:
    def __init__(self, val_produto, quantidade):
        self.val_produto = val_produto
        self.quantidade = quantidade
        self.id_incoterm = str(uuid.uuid4())  # gera um identificador único

    def produto(self):
        return random.choice(produtos)

    def valor_produto(self):
        return random.randint(1, self.val_produto)

    def quantidade_produto(self):
        return random.randint(1, self.quantidade)

    def define_importador(self):
        return random.choice(importadores)

    def define_exportador(self):
        return random.choice(exportadores)

    def flag_negociada(self):
        return random.choice(flags_siscomex)

    def define_paises(self):
        origem = random.choice(paises)
        destino = random.choice(paises)
        # garantir que origem e destino sejam diferentes
        while destino == origem:
            destino = random.choice(paises)
        return origem, destino

    def definido_comex(self):
        produto = self.produto()
        quantidade = self.quantidade_produto()
        valor = self.valor_produto()
        importador = self.define_importador()
        exportador = self.define_exportador()
        flag = self.flag_negociada()
        origem, destino = self.define_paises()

        transaction_def = {
            "id_incoterm": self.id_incoterm,
            "Produto": produto,
            "Quantidade": quantidade,
            "Valor": valor,
            "Importador": importador,
            "Exportador": exportador,
            "Flag": flag,
            "País Origem": origem,
            "País Destino": destino
        }
        print(transaction_def)


if __name__ == "__main__":
    comex_1 = IncotermTransaction(50000, 3000)
    comex_1.definido_comex()
