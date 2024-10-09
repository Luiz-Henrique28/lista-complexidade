def afd_blocos_consecutivos_de_zeros(s):
    estado = 'q0'
    for char in s:
        if estado == 'q0':
            if char == '0':
                estado = 'q1'
        elif estado == 'q1':
            if char == '1':
                estado = 'q2'
            elif char == '0':
                estado = 'q1'
        elif estado == 'q2':
            if char == '0':
                return False
    return True

# Testes
print(afd_blocos_consecutivos_de_zeros("00111"))  # True
print(afd_blocos_consecutivos_de_zeros("010"))    # False
