
saldo = 0
opcao = ''
extrato_saque = []
extrato_deposito = []
cadastro_clientes = {}
cadastro_conta_corrente = {}
tentativas_diarias = 3
agencia = "0001"
numero_conta = 0o0000
resposta = ''
conta = {}

def criar_conta_corrente():
    global cadastro_clientes
    global numero_conta
    global agencia
    global cpf

    cpf = input("digite o seu cpf: ")
    if cpf not in cadastro_clientes:
        print("cpf nao cadastrado na base de dados")
    else:
        resposta = input("Deseja cadastrar uma conta corrente em seu CPF? Digite [s] para sim e [n] para nao ".lower())
        if resposta == 's':
            numero_conta += 1
            conta.update({cpf:{"agencia":agencia, "conta_corrente":numero_conta}})
            print(conta)
        else:
            print("Resposta invalida") 

def visualizar():
    print(cadastro_clientes)
    print(conta)
def cadastrar_usuario():
    global cadastro_clientes
    cpf = input("digite o seu cpf: ")
    if cpf not in cadastro_clientes:
        nome = input("digite o nome: ")
        telefone = input("digite o telefone: ")
        endereco = input("digite o seu endereço: ")
        cadastro_clientes.update({cpf:{"nome":nome, "telefone":telefone, "endereco":endereco}})
        print(cadastro_clientes)
                
    else:
        print("CPF ja cadastrado")

def extrato():
    print('\n-------------------------EXTRATO-------------------------')
    if not extrato_saque:
        print('Não foram realizados saques.')
    else:    
        print('\nHistorico de saque: ')
        [print(f'Saque realizado de: R$ {ext:.2f}')for ext in extrato_saque]
        print(f'Total sacado: R$ {sum(extrato_saque)}')

    if not extrato_deposito:
        print('\nNão foram realizados depositos.')
    else:
     print('\nHistorico de deposito: ')
    [print(f'Deposito realizado de: R$ {ext:.2f}')for ext in extrato_deposito]
    print(f'Total depositado: R$ {sum(extrato_deposito)}')

    print(f'\nSaldo atual é: {saldo:.2f}')
    print('------------------------------------------------------------')
        

def saque():
    global tentativas_diarias
    global saldo
    saque = float(input(('Digite o valor a ser sacado: R$ ')))
    if saque < 0:
        (print('Valor para saque invalido.'))

    elif tentativas_diarias <1:
        print('Numero de saques diarios excedidos.')

    elif saque <= saldo and tentativas_diarias >=1:
        extrato_saque.append(saque)
        print()
        saldo-=saque
        tentativas_diarias -= 1
        print(f'Valor sacado: R$ {saque:.2f}')
        print(f'Seu saldo é: R$ {saldo:.2f}')

    elif saldo < saque:
        print("Seu saldo é insuficiente.")

def depositar():
    global saldo
    deposito = float(input(f'Digite o valor que quer depositar: R$ '))
    if deposito > 0: 
        saldo += deposito
        extrato_deposito.append(deposito)
        print(f'Saldo atual: R$ {saldo:.2f}')
    else:
        print('Valor para deposito invalido.')

while opcao != "x" :
    opcao = (input("Digite [s] para saque - [c] para se cadastrar - [cc] para criar conta corrente - [e] para extrato - [d] para depositar - [x] para sair: ").lower())
    if opcao == "e":
        extrato()

    elif opcao == "s":
        saque()

    elif opcao == "d":
        depositar()
        
    elif opcao == "x":
        break

    elif opcao == "c":
        cadastrar_usuario()

    elif opcao == "cc":
        criar_conta_corrente()    
    elif opcao == "h":
        visualizar() 

    else:
        print('Opção invalida.')    
