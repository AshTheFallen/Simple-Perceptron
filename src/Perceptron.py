import numpy as np

weights = np.zeros((1, 3))
# print(weights)
weight_change = True
# maximum number of loops
max_loop = 100
loop_counter = 0
inputs = np.zeros((4, 3))

# learning rate of perceptron
learning_rate = 0.2
answers = np.zeros((1, 4))

# initialization of values
inputs[0][0] = 1
inputs[1][0] = 1
inputs[2][0] = 1
inputs[3][0] = 1

inputs[0][1] = 0
inputs[1][1] = 1
inputs[2][1] = 0
inputs[3][1] = 1

inputs[0][2] = 1
inputs[1][2] = 1
inputs[2][2] = 0
inputs[3][2] = 0

answers[0][0] = 1
answers[0][1] = 1
answers[0][2] = 0
answers[0][3] = 1

# print(len(weights[0]))
# print(weights[0]@ inputs[0])

for i in range(len(weights[0])):
    weights[0][i] = 1.0


# Perceptron's Code
while loop_counter < max_loop:
    if weight_change is False:
        break
    weight_change = False
    print("loop number {} \n".format( loop_counter))
    for i in range(len(inputs)):
        result = weights[0]@inputs[i]
        if result > 0:
            result = 1
        else:
            result=0
        result = answers[0][i] - (result)
        print(result)
        for j in range(len(weights[0])):
            delta = result* inputs[i][j]*learning_rate
            if delta != 0:
                weight_change = True
                weights[0][j] = weights[0][j] + delta
    print(weight_change)
    print(weights)
    loop_counter = loop_counter +1
