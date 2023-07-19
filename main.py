menu = '''
1 - Deposito\n
2 - Saque\n
3 - extrato\n
0 - sair
'''
VALOR_SAQUE_MAX = 500
saques_realizado = 0
extrato = []
saldo = 0

while True:
    print(menu)
    operacao = int(input('Escolha a operação: '))

    if operacao == 1:
        valor = float(input('Valor do deposito: '))
        if valor > 0:
            saldo += valor
            extrato.append(f'Deposito: R${valor}')
            print('Deposito realizado com sucesso!')
        else:
            print('Valor informado menor ou igaul a 0')

    elif operacao == 2:
        if saques_realizado < 3:
            valor = float(input('Valor do saque: '))
            if valor < saldo and valor <= VALOR_SAQUE_MAX:
                saldo -= valor
                extrato.append(f'Saque: R${valor}')
                print('Saque realizado com sucesso!')
            else:
                print('Saldo insuficiente!')
        else:
            print('Não é possivel realizar saque\n' +
                  f'saques realizados: {saques_realizado}')
        

    elif operacao ==3:
        for e in extrato:
            print(f'{e}\n')
    
    else:
        break