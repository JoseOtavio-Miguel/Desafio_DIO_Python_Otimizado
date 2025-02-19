import os
import textwrap
from verifica_cpf import verifica_cpf
from datetime import datetime

class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self.cliente = cliente
        self._extrato = []
        
        self.limite_saque = 500
        self.limite_transacoes = 3
        
    def __str__(self):
        return f"""\
            Agência:\t{self._agencia}
            C/C:\t{self._numero}
            Titular:\t{self.cliente.nome}
        """

    def adicionar_extrato(self, transacao, valor):
        self._extrato.append(
            {
                "tipo": transacao,
                "valor": valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )
     
    def sacar(self):
        valor = float(input("Informe o valor do saque: "))
        if valor <= self._saldo:
            if self.limite_saque >= valor and self.limite_transacoes > len(self._extrato):
                self._saldo -=valor
                self.adicionar_extrato("Saque", valor)   
            else:
                print(" Limite de Transações Atingido !")    
        else:
            print(" Valor Invalido !")  
                
                
    def depositar(self):
        valor = float(input("Informe o valor do saque: "))
        if valor > 0:
            if self.limite_transacoes > len(self._extrato):
                self._saldo +=valor
                self.adicionar_extrato("Deposito", valor)  
            else:
                print(" Limite de Transações Atingido !")    
        else:
            print(" Valor Invalido !")   
            
            
    def exibir_extrato(self):
        if not self._extrato:
            print("Nenhuma transação realizada.")
            return

        extrato_str = "Extrato da Conta:\n"
        for transacao in self._extrato:
            extrato_str += f"\n{transacao['data']}\n{transacao['tipo']}:\n\t R$ {transacao['valor']:.2f}\n"

        print(extrato_str)
        print(f"\nSaldo:\n\tR$ {self._saldo:.2f}")
        print("==========================================")


class Cliente:
    def __init__(self, endereco):
        self.contas = []
        self.endereco = endereco
        
           
        
class CadastroPessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco  
        

def criar_cliente():
    print("Insira os dados para criar a conta \n ")
    valida_cpf = False
    while (valida_cpf == False):
        cpf = input("Informe o CPF (somente número): ")
        if len(cpf.strip()) == 11  and cpf.isdigit():
            cpf_onze_digitos = cpf
            cpf_nove_digitos = []
            digitos_verificadores = []
            cont = 0
            for digito in cpf_onze_digitos.strip():
                if(cont < 9):
                    cpf_nove_digitos.append(digito)
                    cont+=1
                else:
                    digitos_verificadores.append(digito)
            valida_cpf = verifica_cpf(cpf_nove_digitos, digitos_verificadores)
        else:
            print("Dados Inválidos")
    
    nome = input("Informe o nome completo (Mínimo:12 / Máximo:50 [caracteres]): ")
    # Valida se o nome contem apenas letras e espacos
    while( len(nome) < 10 or len(nome) > 50 or not nome_valido(nome)):
        print(" ERRO - Caracteres inválidos ou fora do Limite ! \n")
        nome = input("Informe o nome completo (Mínimo:12, Máximo:50 [caracteres]): ")

    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    while not validar_data(data_nascimento):
        print("Formato inválido! A data deve estar no formato dd-mm-aaaa e ser válida.")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    
    endereco = input("Informe o endereço (Logradouro, Número, Bairro, Cidade, Sigla Estado): ")
    
    
    cliente = CadastroPessoaFisica(nome, data_nascimento, cpf, endereco)
    return cliente
        

def criar_conta(cliente, contas, numero):
    conta = Conta(cliente, numero)
    conta._numero += 1
    return conta, conta._numero


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    for conta in contas:
        print("=" * 30)
        print("Dados da Conta")
        print(conta)

def validar_data(data):
    try:
        datetime.strptime(data, "%d-%m-%Y")  # Realiza a parse(conversão) da data para o formato específico
        return True
    except ValueError:
        return False  
     
# Função para validar o nome do usuário
def nome_valido(nome):
    return all(char.isalpha() or char.isspace() for char in nome) 
     
     
def main():
    clientes = []
    
 
os.system('cls')
# Menu do Usuário 
def menu():
    # Exibe as opções do Sistema
    menu = """
    ------------ MENU --------------
    [1] - \tDEPOSITAR
    [2] - \tSACAR
    [3] - \tEXTRATO
    [4] - \tCRIAR CONTA
    [5] - \tLISTAR CONTAS
    [6] - \tCRIAR USUARIO
    [0] - \tSAIR
    => """
    return input(textwrap.dedent(menu)) #Remove espaços extras à esquerda da entrada (string[menu])
    
    
def main():
    cliente = criar_cliente()
    contas = []
    numero_contas = 0
    while True:
        opcao = menu()
        
        if opcao == '1':
            conta.depositar()

        elif opcao == '2':
            conta.sacar()

        elif opcao == '3':
            conta.exibir_extrato()

        elif opcao == '4':
            conta, numero_contas = criar_conta(cliente,contas, numero_contas)
            contas.append(conta)
            print(conta)
            
        elif opcao == '5':
            listar_contas(contas)
            
        elif opcao == '6':
            cliente = criar_cliente()
            
            print(cliente.cpf)

        elif opcao == '0':
            break

        else:
            print("\n Código Inválido !")
            print("\n Digite novamente uma Opção (0 para Sair)")


main()