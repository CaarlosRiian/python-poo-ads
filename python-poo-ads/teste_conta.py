from conta import Conta

def cria_conta(self, numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(self, conta, valor):
    conta['saldo'] += valor

def saca(self, conta, valor):
    conta['saldo'] -= valor

def extrato(self, conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))

Conta.deposita(50.0)
Conta.extrato()
Conta.saca(20.0)
Conta.extrato()