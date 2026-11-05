from controller import PessoaController
while True:
    decisao = int(input('Digite 1 para cadastrar uma pessoa ou digite 2 para ler uma pessoa e 3 para sair: '))
    if decisao == 1:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        cpf = input('Digite seu CPF: ')
    if decisao == 3:
        break
        if PessoaController.cadastrar(nome, idade, cpf):
            print('Pessoa cadastrada com sucesso!')
        else:
            print('Digite valores válidos para cadastrar a pessoa!')