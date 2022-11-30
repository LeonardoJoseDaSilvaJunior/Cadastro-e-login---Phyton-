#cadastro do aluno 

nome = str(input('Insira o seu nome: '))
senha = int(input('insira sua senha: '))

def cadastro_inicial():
    print(f'Obrigado por se cadastar na lest´s code!')
    print(f'nome do aluno:{nome} senha:{senha}.')
cadastro_inicial()

nome_aluno = str(input('Insira o seu nome: '))
print('Caso queira encerrar o processo, Digite - " 0 "')
senha_aluno = int(input('insira sua senha: '))
#pagamento da matricula
if senha_aluno != 0:
#login do aluno

    while nome != nome_aluno or senha != senha_aluno:
        print('Nome ou senha, invalidos. Por favor tente novamente')
        nome_aluno = str(input('Insira o seu nome: '))
        senha_aluno = int(input('insira sua senha: '))

    cursos = [' ','python', 'java'] 
    print('ID| Cursos   |')
    print('1 | Python   |')
    print('2 | Java     |')

    identificacao = int(input('insira o ID do curso desejado: '))
    print('')

    while identificacao != 1 and identificacao != 2:  
        print('erro')
        identificacao = int(input('insira um ID valido: '))
    print(f'Curso selecionado: {cursos[identificacao]}')
    print('')
    turno = ['0', 'Manhã','Tarde','noite','Manhã','Tarde', 'noite']
    preco_do_curso = ['', 1000, 1200, 1300, 600, 700, 750]


    print('|               PRESENCIAL             |')
    print('========================================')
    print('|ID| Turno |    Horários     | Preços  |')
    print('|1 | Manhã |  6:00h às 11:00h| R$ 1000 |')
    print('|2 | Tarde | 12:00h às 17:00h| R$ 1200 |')
    print('|3 | Noite | 18:00h às 23:00h| R$ 1300 |')
    print('')
    print('|                  Online              |')
    print('========================================')
    print('|ID| Turno |    Horários     | Preços  |')
    print('|4 | Manhã |    indefinido   | R$ 600  |')
    print('|5 | Tarde |    indefinido   | R$ 700  |')
    print('|6 | Noite |    indefinido   | R$ 750  |')

    id_turno = int(input('insira o ID do turno desejado: '))

    while id_turno != 1 and id_turno != 2 and id_turno != 3 and id_turno != 4 and id_turno != 5 and id_turno != 6:  
        print('erro')
        id_turno = int(input('insira um ID valido: '))
        
    def cadastro_final():
        print(f'Curso: {cursos[identificacao]}')
        print(f'Turno: {turno[id_turno]}')
        print(f'Preço: R$ {preco_do_curso[id_turno]}')
    cadastro_final()

    print("|ID|  formas de pagamento  | ")
    print("|1 |     Débito            | ")
    print("|2 |     Crédito           | ")
#                    formas de pagamento
    formas_de_pagamento = ['','Débito', 'Crédito']
    id_pagamento = int(input('Insira o ID da forma de pagamento desejado: '))
    #pagamento = int(input("Inisira o valor do curso desejado: "))
    while id_pagamento != 1 and id_pagamento != 2:
        print('ID incorreto. Selecione um ID valido: ')
        id_pagamento = int(input('Insira o ID da forma de pagamento desejado: '))

#                          Débito
    if id_pagamento == 1:
        valor = preco_do_curso[id_turno]
        print('Valor do curso: ',valor)
        print(f"Forma de pagamento: {formas_de_pagamento[id_pagamento]}")
        pagamento = int(input(f'Efetue o pagamento: '))

        while pagamento != valor:
            print('valor incorreto')
            print('Valor do curso: ',valor)
            pagamento = int(input(f'Efetue o pagamento: '))

        print('pagamento efetuado, Seja Bem-Vindo à let´s code!')
#                         Crédito
    elif  id_pagamento == 2:
        print(f"Forma de pagamento{formas_de_pagamento[id_pagamento]}")
        print(f'Valor do curso:{preco_do_curso[id_turno]}')
        print('Deseja parcelar? ')
        print('1 = Sim, desejo parcelar        2 - não, muito obrigado' )
        formas_de_pagamento = int(input())
        while formas_de_pagamento != 1 and formas_de_pagamento != 2:
            print('1 = Sim, desejo parcelar        2 - não, muito obrigado' )
            print('Número invalido')
            formas_de_pagamento = int(input())
#Crédito com Parcelas          
        if formas_de_pagamento == 1:
            print('Nós parcelamos em até 2x !')
            parcela_credito = int(input('Quantidade de parcelas: '))  

            while True:
    
                if parcela_credito > 2 or parcela_credito <= 0:
                    print(f'Você digitou: {parcela_credito}. Quantidade de parcelas execeu o limite. Só parcelamos em até 2x')
                    parcela_credito = int(input('Em quantas vezes pretende parcelar? '))    
                    break;

            valor_final = preco_do_curso[id_turno]/parcela_credito
            print('Dividido em ',parcela_credito, 'x')
            print('valor das parcelas: ', valor_final)
            pagamento = int(input(f'Efetue o pagamento: '))

            while pagamento != valor_final: 
               print('valor incorreto')
               print('valor das parcelas: ', valor_final)
               pagamento = int(input(f'Efetue o pagamento: '))
# Crédito sem parcelas
        if  formas_de_pagamento == 2:
            valor_final = preco_do_curso[id_turno]/pagamento
            print('Valor do curso: ',valor_final)
            pagamento = int(input(f'Efetue o pagamento: '))
            while pagamento != valor_final: 
                print('valor incorreto')
                print('valor das parcelas: ', valor_final)
                pagamento = int(input(f'Efetue o pagamento: '))
                
    print('Pagamento efetuado')

else:
    print('Programa encerrado')












