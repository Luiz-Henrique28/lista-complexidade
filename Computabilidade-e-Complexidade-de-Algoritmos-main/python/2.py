def afd_par_de_zeros(s):
    estado = 'q0'
    for char in s:
        if estado == 'q0':
            if char == '0':
                estado = 'q1'
            elif char == '1':
                estado = 'q0'
        elif estado == 'q1':
            if char == '0':
                estado = 'q0'
            elif char == '1':
                estado = 'q1'
    return estado == 'q0'

# Testes
print(afd_par_de_zeros("101"))  # True
print(afd_par_de_zeros("100"))  # False
