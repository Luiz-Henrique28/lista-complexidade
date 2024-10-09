def afd_impar_as(s):
    estado = 'q0'
    for char in s:
        if estado == 'q0' and char == 'a':
            estado = 'q1'
        elif estado == 'q1' and char == 'a':
            estado = 'q0'
    return estado == 'q1'

# Testes
print(afd_impar_as("a"))    # True
print(afd_impar_as("aa"))   # False
print(afd_impar_as("aba"))  # True
