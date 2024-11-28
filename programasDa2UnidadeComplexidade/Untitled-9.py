class AFN3:
    def __init__(self):
        self.state = 'q0'

    def transition(self, char):
        if self.state == 'q0' and char == 'a':
            self.state = 'q1'
        elif self.state == 'q1' and char == 'a':
            self.state = 'q2'

    def is_accepted(self):
        return self.state == 'q1'

    def test(self, input_string):
        self.state = 'q0'
        for char in input_string:
            self.transition(char)
        return self.is_accepted()

# Testes
afn3 = AFN3()
test_cases = ["a", "aa", "bba", "bb", "bab"]
print({case: afn3.test(case) for case in test_cases})
