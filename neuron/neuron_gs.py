
def multiple_neuron_calculate_output(my_weights, my_inputs, bias):
    for i in range(len(my_weights)):
        output = my_inputs[i] * my_weights[i]

    output += bias
    print(output)

def single_neuron_calculate_output(my_weight, my_input, my_bias):
    output = (my_weight * my_input) + my_bias
    print(output)


def n_neuron_input_layer_m_multiple_output(my_weights, my_inputs, my_bias):
    output = np.full_like(my_bias, 0)

    for i in range(len(my_weights)):
        for j in range(len(my_weights[i])):
            # print_neuron_value_by_and_weights_inputs(my_inputs[j], my_weights[i][j])
            output[i] += my_inputs[j] * my_weights[i][j]
        output[i] += my_bias[i]

    print(output)


def output_single_neuron_with_numpy(inputs, weights, bias):
    my_output = np.dot(weights,inputs) + bias
    return my_output

def print_neuron_value_by_and_weights_inputs(my_weights, my_inputs):
    print("multiplies", my_weights, "x", my_inputs)



