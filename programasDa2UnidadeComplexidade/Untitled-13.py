class MT3:
    def __init__(self):
        self.state = 'q0'

    def transition(self, char):
        if self.state == 'q0' and char == 'a':
            self.state = 'q1'
        elif self.state == 'q1' and char == 'b':
            self.state = 'q0'
        else:
            self.state = 'q_reject'

    def is_accepted(self):
        return self.state == 'q0'

    def test_mt3(self, input_string):
        self.state = 'q0'
        for char in input_string:
            self.transition(char)
            if self.state == 'q_reject':
                return False
        return self.is_accepted()

# Testes
mt = MT3()
test_cases = ["", "ab", "abab", "aba", "ababab"]
results = {case: mt.test_mt3(case) for case in test_cases}
print(results)
