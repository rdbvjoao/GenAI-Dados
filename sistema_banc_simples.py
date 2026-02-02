saldo = 5000

try:
    tipo_conta = int(input("Informe o tipo da conta:\n1 - Conta Normal\n2 - Conta Universitária: "))
except ValueError:
    print("Entrada inválida. Digite um número.")
    exit()



def sacar(saldo, tipo_conta):
    valor = float(input("Digite o valor a ser sacado: "))

    if valor <= 0:
        print("Valor inválido!")
        return saldo

    if tipo_conta == 2 and valor > 500: 
        print("Conta Universitária! O saque máximo de R$ 500 por cada operação!")
        return saldo
    
    
    if saldo >= valor:
        saldo -= valor
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
    

    return saldo



def depositar(saldo, tipo_conta):

    valor = float(input("Digite o valor de depósito: "))

    if valor <= 0:
        print("Valor inválido para depósito!")
        return saldo


    if tipo_conta == 2 and valor > 2000:
        print("Conta Universitária! O valor de depósito máximo é de R$ 2000 por operação!")
        return saldo
    

    saldo += valor
    print("Valor depositado com sucesso!")

    return saldo



def extrato(tipo_conta,saldo):
    
    largura = 50; #Utilizando a largura para centralizar o menu de opções

    print("\n"+" Extrato  da Conta ".center(largura, "="))
    
    if tipo_conta == 1:
        print("Tipo da conta: Conta Normal")
        print("Benefício: operações de saques e depósitos ilimitados")
    elif tipo_conta == 2:
        print("Tipo da conta: Conta Universitária")
        print("Benefício da conta: sem taxa de manutenção e limite menor de saque/depósito")
    else:
        print("Tipo da conta: Desconhecida")

    print(f"Saldo atual: R$ {saldo:.2f}")
    print("="*largura)


def investir(saldo):
    valor = float(input("Digite o valor a ser investido: "))
    
    if valor <= 0:
        print("Valor inválido para investimento!")
        return saldo
    if valor > saldo:
        print("Saldo insuficiente para investir!")
        return saldo
    
    rendimento = valor * 0.05
    saldo += rendimento
    print(f"Investimento realizado! Rendimento de R$ {rendimento:.2f} adicionado ao saldo.")
    
    return saldo




def mostrar_menu():
    
    largura = 50

    print("\n" + " Menu Principal de Opções ".center(largura, "="))

    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Extrato")
    print("4 - Sair")

    if tipo_conta == 1:
        print("5 - Investir dinheiro")

    if tipo_conta == 2:
        print("Importante! O saque máximo é de R$ 500 e depósito máximo R$ 2000")
    
    print("="*largura)



if tipo_conta not in (1,2):
    print("Conta não encontrada, entre em contato com seu gerente!")
else:
    while True:
        
        mostrar_menu()
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite um número válido: ")
            continue

        if opcao == 1:
            saldo = sacar(saldo,tipo_conta)

        elif opcao == 2:
            saldo = depositar(saldo,tipo_conta)

        elif opcao == 3:
            extrato(tipo_conta, saldo)

        elif opcao == 4:
            print("\nTarefa finalizada\nObrigado por utilizar nossos serviços!")
            break

        elif opcao == 5 and tipo_conta == 1:
            saldo = investir(saldo)

        else:
            print("Opção inválida!")
