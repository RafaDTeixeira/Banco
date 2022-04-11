from Banco import Banco

def menu():
    return input('1. Deposito\n' \
           '2. Retirar\n' \
           '3. Exibir Dados\n' \
           '4. Consultar Saldo\n' \
           '5. Extrato\n' \
           '6. Encerrar\n' \
           'Opção: ')


ban = Banco()
while True:
    print('~' * 50)
    print(ban.Banco())
    print('~' * 50)
    op = menu()
    if op == '1':
        ban.deposito()
    elif op == '2':
        ban.retirar()
    elif op == '3':
        ban.resumo()
    elif op == '4':
        ban.__saldo()
    elif op == '5':
        ban.extrato()
    elif op == '6':
        break
    else:
        print('Opção Errada!')