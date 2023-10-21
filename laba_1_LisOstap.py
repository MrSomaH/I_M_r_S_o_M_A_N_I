class Neuron:
    def __init__(self, *weight_coefficients):
        self.coefficients = weight_coefficients
    
    def output(self, *input_values):
        input_values = list(input_values)
        input_values.insert(0, 1)
        list_length = len(input_values) 
        if list_length == len(self.coefficients):
            self.d_value = sum([self.coefficients[i] * input_values[i] for i in range(list_length)]) 
            return 0 if self.d_value <= 0 else 1
        else:
            raise Exception("The length of weight-coefficients and input_values does not coincide")

    def NOT(self, x):
        # Операція заперечення (NOT)
        return 1 - x
    
    def XOR(self, x, y):
        # Операція стрілки Пірсона (XOR)
        return self.output(self.NOT(self.output(x, y)), self.output(x, y))

# Створення об'єктів для операцій NOT і XOR
neuron_not = Neuron(-1, 1)  # Ваги налаштовані для NOT
neuron_xor = Neuron(-0.5, 1, 1)  # Ваги налаштовані для XOR

# Перевірка операцій NOT і XOR
print("NOT 0:", neuron_not.output(0))
print("NOT 1:", neuron_not.output(1))

print("XOR 0, 0:", neuron_xor.output(0, 0))
print("XOR 0, 1:", neuron_xor.output(0, 1))
print("XOR 1, 0:", neuron_xor.output(1, 0))
print("XOR 1, 1:", neuron_xor.output(1, 1))

'''neuron_and = Neuron(-1.5, 1, 1)

print(neuron_and.output(0, 0))
print(neuron_and.output(0, 1))
print(neuron_and.output(1, 0))
print(neuron_and.output(1, 1))

neuron_or = Neuron(-1.5, 2, 2)

print(neuron_or.output(0, 0))
print(neuron_or.output(0, 1))
print(neuron_or.output(1, 0))
print(neuron_or.output(1, 1))

neuron_and_1 = Neuron(-1.5, 1, 1)
neuron_and_2 = Neuron(-1.5, 1, 1)
neuron_or_1 = Neuron(-1.5, 2, 2)
neuron_or_2 = Neuron(-1.5, 2, 2)'''
