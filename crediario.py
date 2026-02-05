precoavistacelular = float (input (" Qual o valor avista do celular ? "))
print()
entradainicial = precoavistacelular * 0.33 

print ("recomendo dar entrada incial de : ", entradainicial)
print()

entrada = float (input("consegue dar a entrada do valor recomendado ? se sim coloque o valor igual ou acima do que foi informado anteriormente:\n"))
print()
if entrada > entradainicial:
    print("vamos prosseguir")
    print()
elif entrada == entradainicial:
    print("vamos prosseguir")
    print()
else:
    print("vamos negociar a entrada para conseguir atender o seu pedido")
    print()

pagamento = str (input("pagamento é semanal, quinzena ou mensal ? Responda com as seguintes Letras -- S = semanal Q - Quinzena e M - mensal ---?\n"))

if pagamento in ['s' , 'S' , 'Q', 'q']:
    semanal = 0.15
    valordojuros = precoavistacelular * semanal 
    valorfinal = valordojuros + precoavistacelular


elif pagamento in ['M' , 'm']:
    mensal = 0.20
    valordojuros = precoavistacelular * mensal
    valorfinal = valordojuros + precoavistacelular
    
else:
    valorfinal = "Opção inválida"
    valordojuros = 0
    
print("valor inicial é ", precoavistacelular)
print("O valor final com o juros é ", valorfinal)

parcela = int (input(" quantas parcela deseja parcela ? "))

if parcela < 5:
    valorparcela = valorfinal - entrada
    print("valor restante que sera parcelado", valorparcela)
    parcelafinal = valorparcela / parcela
    print(parcelafinal)
    
elif parcela == 5:
    valorparcela = valorfinal - entrada
    print("valor restante que sera parcelado", valorparcela)
    parcelafinal = valorparcela / parcela
    print(parcelafinal)
    
else:
    parcela > 5
    print(" Não podemos fazer mais do 5 parcelas")
    
