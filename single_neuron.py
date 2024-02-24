import random

import numpy as np


# class Neuron {
#     protected calculate_n_layers_neuron():
#
# }

def calculate_n_layers_neuron(inputs, weights, biases):
    layer_outputs = []

    for neuron_weights, neuron_bias in zip(weights, biases):
        neuron_output = 0

        for n_input, weights in zip(inputs, neuron_weights):
            neuron_output += n_input * weights

        neuron_output += neuron_bias
        layer_outputs.append(neuron_output)

    return layer_outputs


def multiple_neuron_calculate_output(my_weights, my_inputs, bias):
    for i in range(len(my_weights)):
        output = my_inputs[i] * my_weights[i]
    output += bias
    return output


def single_neuron_calculate_output(my_weight, my_input, my_bias):
    output = (my_weight * my_input) + my_bias
    print(output)


def multiple_layer__neuron_input_layer_multiple_output(my_weights, my_inputs, my_bias):
    output = np.full_like(my_bias, 0)

    for i in multiple_neuron_calculate_output(my_weights, my_inputs, my_bias):
        output
    for i in range(len(my_weights)):
        for j in range(len(my_weights[i])):
            output[i] += my_inputs[j] * my_weights[i][j]
        output[i] += my_bias[i]

    print(output)


def output_single_neuron_with_numpy(inputs, weights, bias):
    my_output = np.dot(weights, inputs) + bias
    return my_output


def multiply_n_matrix(matrices):
    for matrix in range(matrices):
        output = matrix ** matrix

    return output


def print_neuron_value_by_and_weights_inputs(my_weights, my_inputs):
    print("multiplies", my_weights, "x", my_inputs)


def create_tensor(m):
    print(m)

    # output = np.matmul(m[])
    # return output


def reshape(matrix):
    print(matrix)
    # np.reshape(matrix, )


def generate_random_array_inputs(quantity):
    return np.full(shape=quantity, fill_value=random.choice([True, False]))


def generate_random_weights_inputs(min_value, max_value):
    return random.uniform(min_value, max_value)

    # return

# test_data = {
#
#     inputs = {1, 2, 3},
#     weights = [0.2, 0.8, -0.5],
#
# }

# %%
