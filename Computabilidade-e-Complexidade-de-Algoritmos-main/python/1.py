def afd_termina_com_1(s):
    estado = 'q0'
    for char in s:
        if estado == 'q0':
            if char == '0':
                estado = 'q0'
            elif char == '1':
                estado = 'q1'
        elif estado == 'q1':
            if char == '0':
                estado = 'q0'
            elif char == '1':
                estado = 'q1'
    return estado == 'q1'

# Testes
print(afd_termina_com_1("101"))  # True
print(afd_termina_com_1("100"))  # False
