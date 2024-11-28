class MT1:
    def __init__(self):
        self.state = 'q0'  # Estado inicial
        self.tape = ['#']  # Fita inicializada com o símbolo vazio
        self.head_position = 0  # Cabeça de leitura na posição inicial

    def transition(self):
        if self.state == 'q0' and self.tape[self.head_position] == '#':
            self.state = 'q_accept'  # Transição para o estado de aceitação

    def is_accepted(self):
        return self.state == 'q_accept'

    def test_mt1(self, input_string):
        # Configurar a fita com a entrada e adicionar o símbolo de fim
        self.tape = list(input_string) + ['#']
        self.state = 'q0'
        self.head_position = 0

        # Executar a transição até que a máquina alcance um estado final
        while self.state != 'q_accept':
            self.transition()

        return self.is_accepted()

# Testes
mt = MT1()
test_cases = ["", "a", "ab", "baba"]
results = {case: mt.test_mt1(case) for case in test_cases}
print(results)
