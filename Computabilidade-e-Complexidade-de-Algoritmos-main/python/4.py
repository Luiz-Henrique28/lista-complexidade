def afd_ao_menos_um_zero(s):
    estado = 'q0'
    for char in s:
        if estado == 'q0' and char == '0':
            estado = 'q1'
    return estado == 'q1'

# Testes
print(afd_ao_menos_um_zero("110"))  # True
print(afd_ao_menos_um_zero("111"))  # False
