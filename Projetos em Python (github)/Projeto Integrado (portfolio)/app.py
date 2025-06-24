class Produto:
    def __init__(self, codigo, descricao, preco, quantidade, localizacao):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        self.localizacao = localizacao

class Estoque:
    def __init__(self):
        self.produtos = {}
    
    def cadastrar_produto(self, produto):
        self.produtos[produto.codigo] = produto
        print(f'Produto {produto.descricao} cadastro com sucesso. ')

    def atualizar_estoque(self, codigo, quantidade):
        if codigo in self.produtos:
            self.produtos[codigo].quantidade = quantidade
            print(f'Estoque do produto {self.produtos[codigo].descricao} atualizada com sucesso.')
        else:
            print('Produto nao encontrado')

def rastrear_localizacao(self, codigo):
    if codigo in self.produtos:
            print(f'localizacao do produto {self.produto[codigo].descricao} : {self.produtos[codigo].localizacao}')
    else:
            print("Produto não encontrado.")


def gerar_relatorio(self):
    print('Relatorio de Estoque.')
    for produto in self.produtos.values():
        print(f'Codigo: {produto.codigo}, Descricao: {produto.descricao}. Preco: {produto.preco}, Quantidade : {produto.quantidade}, Localizacao : {produto.localizacao}')

def main():
    estoque = Estoque()

    while True:
        print('\nSistema de estoque')
        print('1. Cadastro de Produto')
        print('2. Atualizacao de Estoque')
        print('3. Rastrear')
        print('4. Gerar Relatório')
        print('5. Sair')

        opcao_escolhida = input('Escolha uma opcao: ')

        if opcao_escolhida == "1":
            codigo = input("Digite o código do produto: ")
            descricao = input("Digite a descrição do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            localizacao = input("Digite a localização do produto: ")
            produto = Produto(codigo, descricao, preco, quantidade, localizacao)
            estoque.cadastrar_produto(produto)
        elif opcao_escolhida == "2":
            codigo = input("Digite o código do produto: ")
            quantidade = int(input("Digite a nova quantidade: "))
            estoque.atualizar_estoque(codigo, quantidade)
        elif opcao_escolhida == "3":
            codigo = input("Digite o código do produto: ")
            estoque.rastrear_localizacao(codigo)
        elif opcao_escolhida == "4":
            estoque.gerar_relatorio()
        elif opcao_escolhida == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
        main()