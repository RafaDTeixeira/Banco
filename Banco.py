class Banco:
    def __init__(self, nome, numero, deposito, retirar, extrato ,saldo=0):
        self.nome = nome
        self.numero = numero
        self.__saldo = 0
        self.deposito = deposito
        self.retirar = retirar
        self.extrato = extrato
    
    def resumo(self):
        print(f'Nome Proprietario da conta {self.nome}\n - Nº da conta {self.numero}\n - Saldo {self.__saldo}')

    @property
    def saldo(self):
        return self.__saldo

    def deposito(self, valor):   
        self.__saldo += valor
        print('Foi realizado um deposito no valor de:', valor)

    def poderet(self, valor):
        return self.__saldo >= valor

    def retirar(self,valor):
        if self.poderet(valor):
            self.__saldo -= self.valor
            print('Foi retirado:', valor)
            return True
        else:
            print("Saldo insuficiente!")
            return False
