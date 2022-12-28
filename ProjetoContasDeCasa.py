continuar = 's'
tipo = 'e'
entradas = []
valoresEntradas = []
somaEntradas = 0
saidas = []
valoresSaidas = []
somaSaidas = 0
while continuar =='s':
    tipo = input('Quer digitar uma entrada ou saída? [E/S]').lower()
    if tipo == 'e':
        nomeEntrada = input('Digite o nome da entrada')
        entradas.append(nomeEntrada)
        valorEntrada = float(input(f'Digite o valor da entrada {nomeEntrada}'))
        valoresEntradas.append(valorEntrada)
        somaEntradas = somaEntradas + valorEntrada
    if tipo == 's':
        nomeSaida = input('Digite o nome da saida')
        saidas.append(nomeSaida)
        valorSaida = float(input(f'Digite o valor da saida {nomeSaida}'))
        valoresSaidas.append(valorSaida)
        somaSaidas = somaSaidas + valorSaida
    continuar  = input('Quer continuar a inserir? [S/N]').lower()
somaFinal = somaEntradas - somaSaidas

if somaFinal >0:
    mensagemFinal = f'Parabéns, você encerrou esse período com saldo positivo de {somaFinal}'
elif somaFinal <0:
    mensagemFinal = f'Infelizmente você ainda estpa devendo {somaFinal}'
else:
    mensagemFinal = 'Você finalizou no 0, melhor que estar devendo!'

print(f'''
As entradas foram {entradas}, 
com os respectivos valores {valoresEntradas},
somando um total de entradas {somaEntradas}.

As saidas foram {saidas}, 
com os respectivos valores {valoresSaidas},
somando um total de saidas {somaSaidas}.

O saldo total é {somaFinal}''')

print(mensagemFinal)

