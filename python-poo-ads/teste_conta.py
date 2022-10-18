from conta import Conta, Cliente

cliente1 = Cliente('Robert', 'Diniz', 165141365561)
conta1 = Conta(2022, cliente1.nome, 150, 1500)

conta1.deposita(50.0)
conta1.extrato()
conta1.saca(20.0)
conta1.extrato()
conta1.historico.imprime()

