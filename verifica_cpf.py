# Função que verifica se o CPF informado é valido
def verifica_cpf(cpf : list, digitos_verificadores : list):
    contador = 10
    resultados = []
    for digito in cpf:
        calculo = (int(digito) * contador )
        #print(calculo, contador)
        resultados.append(calculo)
        contador -=1
        
    # Divide o resultado da soma dos digitos por onze
    soma_digitos = sum(resultados)
    #print(f'Soma:  {soma_digitos}')
    resto_divisao  = (soma_digitos % 11)
    #print(f'Calculo digito 1 : {resto_divisao}')
    
    if (resto_divisao == 0 or resto_divisao == 1):
        digito_1 = 0
    else:
        digito_1 = 11 - resto_divisao
        
    #print(f'O primeiro digito verificador é : {digito_1}')
    
    contador = 11
    resultados = []
    cpf.append(digito_1)
    for digito in cpf:
        #print(digito)
        calculo = (int(digito) * contador )
        #print(calculo, contador)
        resultados.append(calculo)
        contador -=1
        
    # Divide o resultado da soma dos digitos por onze
    soma_digitos = sum(resultados)
    #print(f'Soma:  {soma_digitos}')
    resto_divisao  = (soma_digitos % 11)
    #print(f'Calculo digito 2 : {resto_divisao}')
    
    if (resto_divisao == 0 or resto_divisao == 1):
        digito_2 = 0
    else:
        digito_2 = 11 - resto_divisao
        
    if(digito_1 == int(digitos_verificadores[0]) and digito_2 == int(digitos_verificadores[1])):
        print("--- CPF VÁLIDO ---")
        return True
    else:
        print("--- CPF INVÁLIDO ---")
        return False

