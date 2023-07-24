menu = """

*------- BEM-VINDO AO BANCO : MONTE PYTHON -------*

Escolha a operação Desejada :

[1] Depositar

[2] Sacar

[3] Extrato

[4] Sair

=> """

saldo = 0

limite = 500

extrato = ""

numero_saques = 0

LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == "1":

    dep = (float(input('Qual valor do depósito: R$')))

    if dep > 0:

      saldo += dep

      print('Depósito Realizado com Sucesso!')

      extrato += (f'\nDepósito: R$ {dep:.2f}')

    else:

      print('Operação Não Sucedida. Informe um valor válido!')         

  elif opcao == "2":

    saq = (float(input("Qual valor você deseja sacar? ")))

    excedeu_saldo = saq > saldo 
    
    excedeu_limite = saq > limite



    excedeu_saques = numero_saques >= LIMITE_SAQUES
    

    if excedeu_saldo:

      print('Operação falhou!  Saldo Insuficiente.')

    elif excedeu_limite:

      print ('Operação falhou o valor Estourou o Limite.')

    elif excedeu_saques:

      print('Operação falhou! Número máximo de saques excedido')

    elif sq > 0:

      saldo -= sq

      extrato += f'Saque: R$ {sq:.2f}\n'

      numero_saques += 1

    
    else:

      print('Operação Falhou! O valor é inválido.')      


  elif opcao == "3":

    depositos = saldo

    print('\n----------EXTRATO --------------')

    print('Não foram Concluídas as  movimentações.' if not extrato else extrato)

    print(f'\nSaldo: R$ {saldo:.2f}')

    print('----------------------------------')


  elif opcao == "4":

    break

  else:

    print("Operação inválida, Tente Novamente.")
