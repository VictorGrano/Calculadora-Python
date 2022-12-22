""""Calculadora com While"""

while True:
    print('Digite os números:')
    num1 = input('Primeiro número: ')
    num2 = input('Segundo número número: ')
    operador = input('Digite o operador(+-*/): ')
    num1_conv = 0
    num2_conv = 0
    verifica_num = None
    operadores = '+-/*'
    try:
        num1_conv = float(num1)
        num2_conv = float(num2)
        verifica_num = True
    except:
        verifica_num = None

    if verifica_num is None:
        print('Um ou mais números são inválidos!')
        continue
    if operador not in operadores:
        print('Operador inválido!')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    if operador == '+':
        resultado = num1_conv + num2_conv
        print(f"O Resultado é {resultado}")
    if operador == '-':
        resultado = num1_conv - num2_conv
        print(f"O Resultado é {resultado}")
    if operador == '*':
        resultado = num1_conv * num2_conv
        print(f"O Resultado é {resultado}")
    if operador == '/':
        resultado = num1_conv / num2_conv
        print(f"O Resultado é {resultado}")

    sair = input('Quer sair? [s]im: ')
    sair = sair.lower().startswith('s')
    if sair:
        break
