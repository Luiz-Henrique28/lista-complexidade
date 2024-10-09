# Máquina de Turing 1 - Incrementa Binário - Universal
# Autor: Ricardo Roberto de Lima - Data: 11/08/2024.


def incrementa_binario(fita):
    """
    Incrementa um número binário representado em uma fita.
    Args:
        fita (list): Lista representando a fita.
    Returns:
        list: Fita com o número incrementado.
    """
    # Implementar a lógica da máquina de Turing aqui
    # ... (Exemplo simplificado)
    # Encontrar o bit menos significativo

    i = len(fita) - 1
    while i >= 0 and fita[i] == '1':
        fita[i] = '0'
        i -= 1
    if i >= 0:
        fita[i] = '1'
    else:
        fita.insert(0, '1')  # Adicionar um bit mais significativo

    return fita

# Exemplo de uso:
fita = ['1', '0', '1']
resultado = incrementa_binario(fita)
print(resultado)  # Saída: ['1', '1', '0']
