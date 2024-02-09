# Calculadora com while

entrar = input('Vamos fazer contas "+, -, *, /"? [S] ou [N]: ').startswith('s')
red_flag = None

while entrar == True:
    primeiro = input('Digite um numero: ')
    segundo = input('Digite outro numero: ')
    operador = input('Operador: ')
    
    try:
        primeiro_n = float(primeiro)
        segundo_n = float(segundo)
        red_flag = True
    except:
        print('Um ou mais números digitados são inválidos.')
        red_flag = None
        continue


    if len(operador) > 1:
        print('Operador inválido')
        continue

    if red_flag is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_validos = '+-*/'

    if operador not in operadores_validos:
        print('Operador iniválido.')
        continue 



    if operador == '+':
        print(primeiro_n + segundo_n)
    elif operador == '-':
        print(primeiro_n - segundo_n)
    elif operador == '*':
        print(primeiro_n * segundo_n)
    elif operador == '/':
        print(primeiro_n // segundo_n)
    else:
        print('Operação inválida.')
        continue

    continuar = input('Deseja sair? ').lower().startswith('s')
    if continuar == True:
        
        break
    
print ('Obrigado por usar nossa calculadora!')
