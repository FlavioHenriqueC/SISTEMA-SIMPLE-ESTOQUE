class Produto:
    def __init__(self, nome, categoria, quantidade, preco, localizacao):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.quantidade} unid. | R${self.preco} | Local: {self.localizacao}'


class Estoque:
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self, produto):
        if produto.nome not in self.produtos:
            self.produtos[produto.nome] = produto
            print(f'{produto.nome} cadastrado.')
        else:
            print(f'{produto.nome} já existe.')

    def consultar_produto(self, nome):
        return self.produtos.get(nome, 'Produto não encontrado.')

    def atualizar_estoque(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome].quantidade += quantidade
            print(f'Estoque de {nome} atualizado.')
        else:
            print('Produto não encontrado.')

    def rastrear_localizacao(self, nome):
        return f'Localização: {self.produtos[nome].localizacao}' if nome in self.produtos else 'Produto não encontrado.'

    def gerar_relatorio(self):
        print("Relatório de Estoque:")
        for p in self.produtos.values():
            print(p)
        print("\nEstoque baixo:")
        for p in self.produtos.values():
            if p.quantidade < 5:
                print(f'{p.nome} ({p.quantidade} unid.)')

        print("\nExcesso de Estoque:")
        for p in self.produtos.values():
            if p.quantidade > 100:
                print(f'{p.nome} ({p.quantidade} unid.)')


class MovimentacaoEstoque:
    def __init__(self):
        self.movimentacoes = []

    def registrar_movimentacao(self, nome, quantidade, tipo):
        self.movimentacoes.append({'nome': nome, 'quantidade': quantidade, 'tipo': tipo})
        print(f'{tipo.capitalize()} de {quantidade} {nome}.')

    def gerar_relatorio_movimentacoes(self):
        print("\nRelatório de Movimentações:")
        for m in self.movimentacoes:
            print(f'{m["tipo"].capitalize()} - {m["nome"]}: {m["quantidade"]} unid.')


# Exemplo de uso
estoque = Estoque()

produto1 = Produto("Teclado", "Eletrônicos", 50, 100.0, "Depósito A1")
produto2 = Produto("Mouse", "Eletrônicos", 10, 50.0, "Depósito B2")

estoque.cadastrar_produto(produto1)
estoque.cadastrar_produto(produto2)

estoque.atualizar_estoque("Mouse", 5)
print(estoque.consultar_produto("Teclado"))
print(estoque.rastrear_localizacao("Mouse"))

estoque.gerar_relatorio()

movimentacao = MovimentacaoEstoque()
movimentacao.registrar_movimentacao("Teclado", 20, "saida")
movimentacao.registrar_movimentacao("Mouse", 5, "entrada")

movimentacao.gerar_relatorio_movimentacoes()
