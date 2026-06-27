def rodar():
    saldo = 1000.00
    carrinho = {}
 
    produtos = {
        1: { 'nome': 'Processador', 'preço': 500.00},
        2: { 'nome': 'Monitor', 'preço': 250.00},
        3: { 'nome': 'HD 1T', 'preço': 50.00}
    }
 
    print('=' * 40)
    print(' BEM-VINDO CARA! de boas? qual seu nome meu caro ')
    nome2 = input("Digite seu nome aqui: ")
    print('=' * 40)
    print(f'Então senhor(a) {nome2}, olhei aqui no nosso sistema e você tem R$ {saldo:.2f} para gastar.')
 
    while True:
        print('\n--- PRODUTOS DISPONÍVEIS ---')
        for codigo, info in produtos.items():
            print(f'[{codigo}] {info["nome"]} - R$ {info["preço"]:.2f}')
 
        print('[V] Ver Carrinho e Pagar')
        print('[S] Sair do Jogo')
        print('-' * 28)
 
        escolha = input('Escolha uma opção: ').strip().upper()
 
        
        if escolha.isdigit() and int(escolha) in produtos:
            codigo_item = int(escolha)
            item = produtos[codigo_item]
 
            
            try:
                qtd = int(input(f'Quantas unidades de {item["nome"]} você quer? '))
                if qtd <= 0:
                    print('Quantidade inválida! Digite um número maior que zero.')
                    continue
            except ValueError:
                print('Por favor, digite um número inteiro válido.')
                continue
 
            custo = item['preço'] * qtd
 
            
            if custo <= saldo:
                saldo -= custo
                nome_produto = item['nome']
 
                
                if nome_produto in carrinho:
                    carrinho[nome_produto] += qtd
                else:
                    carrinho[nome_produto] = qtd
 
                print(f'-> {qtd}x {nome_produto} adicionado(s)!')
                print(f'Saldo restante: R$ {saldo:.2f}')
            else:
                print('Vix {nome2}... saldo insuficiente para esta compra!')
 
        elif escolha == 'V':
            print('\n' + '*' * 2 + '=' * 30)
            print(' SEU CARRINHO ')
            print('=' * 30)
 
            if not carrinho:
                print('Seu carrinho está vazio!')
            else:
                for produto, qtd in carrinho.items():
                    print(f'- {produto}: {qtd}x')
 
            print('-' * 30)
            print(f'Saldo restante: R$ {saldo:.2f}')
            print('-' * 30)
 
            if carrinho:
                confirmar = input('Deseja finalizar a compra e pagar? (S/N): ').strip().upper()
                if confirmar == 'S':
                    print(f'\nCompra finalizada com sucesso! muito obrigado {nome2}, Volte sempre.')
                    break
 
        elif escolha == 'S':
            print('\nVocê saiu do mercadinho.')
            break
 
        else:
            print('Opção inválida! Escolha um código do menu ou V/S.')


rodar()