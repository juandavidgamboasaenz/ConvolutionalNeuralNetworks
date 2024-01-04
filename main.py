# This is a sample Python script.
import single_neuron


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def execute():
    inputs = [1, 2, 3, 2.5]
    weights = [
        [0.2, 0.8, -0.5, 1.0],
        [0.5, -0.91, 0.26, -0.5],
        [-0.26, -0.27, 0.17, 0.87],
    ]
    bias = [2, 3.0, 0.5]
    # Yse
    single_neuron.n_neuron_input_layer_m_multiple_output(weights, inputs, bias)
    output = single_neuron.calculate_n_layers_neuron(inputs, weights, bias)
    print(output)

    # Press the green button in the gutter to run the script.
    # if __name__ == "__main__":


execute()
# single_neuron.generate_random_array_inputs()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# %%
