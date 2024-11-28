class MT2:
    def __init__(self):
        self.state = 'q0'

    def transition(self, char):
        if self.state == 'q0' and char == 'a':
            self.state = 'q1'
        elif self.state == 'q1' and char == 'a':
            self.state = 'q0'

    def is_accepted(self):
        return self.state == 'q0'

    def test_mt2(self, input_string):
        self.state = 'q0'
        for char in input_string:
            self.transition(char)
        return self.is_accepted()

# Testes
mt = MT2()
test_cases = ["", "a", "aa", "aaa", "aaaa"]
results = {case: mt.test_mt2(case) for case in test_cases}
print(results)
