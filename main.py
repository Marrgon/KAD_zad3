import numpy as np
import matplotlib.pyplot as plt


# np.random.seed(0)
def OR():
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(x):
        return x * (1 - x)

    # Input datasets
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    expected_output = np.array([[0], [1], [1], [1]])

    epochs = 20000
    lr = 0.8
    inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons = 2, 2, 1

    # Random weights and bias initialization
    hidden_weights = np.random.uniform(size=(inputLayerNeurons, hiddenLayerNeurons))
    hidden_bias = np.random.uniform(size=(1, hiddenLayerNeurons))
    output_weights = np.random.uniform(size=(hiddenLayerNeurons, outputLayerNeurons))
    output_bias = np.random.uniform(size=(1, outputLayerNeurons))

    print("Initial hidden weights: ", end='')
    print(*hidden_weights)
    print("Initial hidden biases: ", end='')
    print(*hidden_bias)
    print("Initial output weights: ", end='')
    print(*output_weights)
    print("Initial output biases: ", end='')
    print(*output_bias)
    epoch_list = []
    error_history = []

    # Training algorithm

    for j in range(epochs):
        # Forward Propagation
        hidden_layer_activation = np.dot(inputs, hidden_weights)
        hidden_layer_activation += hidden_bias
        hidden_layer_output = sigmoid(hidden_layer_activation)

        output_layer_activation = np.dot(hidden_layer_output, output_weights)
        output_layer_activation += output_bias
        predicted_output = sigmoid(output_layer_activation)

        # Backpropagation
        #error = expected_output - predicted_output
        epoch_list.append(j)
        #print(epoch_list)

        error = expected_output - predicted_output

        error_history.append(np.average(np.abs(error)))
        # print(error_history)
        # e =  error.append(np.average(np.abs(error)))
        # e =  error.append(np.average(np.abs(error)))

        d_predicted_output = error * sigmoid_derivative(predicted_output)

        error_hidden_layer = d_predicted_output.dot(output_weights.T)

        d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

        # Updating Weights and Biases
        output_weights += hidden_layer_output.T.dot(d_predicted_output) * lr
        output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
        hidden_weights += inputs.T.dot(d_hidden_layer) * lr
        hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr

    print("Final hidden weights: ", end='')
    print(*hidden_weights)
    print("Final hidden bias: ", end='')
    print(*hidden_bias)
    print("Final output weights: ", end='')
    print(*output_weights)
    print("Final output bias: ", end='')
    print(*output_bias)

    print("\nOutput from neural network after 10,000 epochs: ", end='')
    print(*predicted_output)

    plt.figure(figsize=(15, 5))
    plt.plot(epoch_list, error_history)
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.show()


def AND():
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(x):
        return x * (1 - x)

    # Input datasets
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    expected_output = np.array([[0], [0], [0], [1]])

    epochs = 20000
    lr = 0.8
    inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons = 2, 2, 1

    # Random weights and bias initialization
    hidden_weights = np.random.uniform(size=(inputLayerNeurons, hiddenLayerNeurons))
    hidden_bias = np.random.uniform(size=(1, hiddenLayerNeurons))
    output_weights = np.random.uniform(size=(hiddenLayerNeurons, outputLayerNeurons))
    output_bias = np.random.uniform(size=(1, outputLayerNeurons))

    print("Initial hidden weights: ", end='')
    print(*hidden_weights)
    print("Initial hidden biases: ", end='')
    print(*hidden_bias)
    print("Initial output weights: ", end='')
    print(*output_weights)
    print("Initial output biases: ", end='')
    print(*output_bias)
    epoch_list = []
    error_history = []

    # Training algorithm

    for j in range(epochs):
        # Forward Propagation
        hidden_layer_activation = np.dot(inputs, hidden_weights)
        hidden_layer_activation += hidden_bias
        hidden_layer_output = sigmoid(hidden_layer_activation)

        output_layer_activation = np.dot(hidden_layer_output, output_weights)
        output_layer_activation += output_bias
        predicted_output = sigmoid(output_layer_activation)

        # Backpropagation

        # error = expected_output - predicted_output
        epoch_list.append(j)
        # print(epoch_list)

        error = expected_output - predicted_output

        error_history.append(np.average(np.abs(error)))
        # print(error_history)
        # e =  error.append(np.average(np.abs(error)))
        # e =  error.append(np.average(np.abs(error)))
        # error_history = [np.average(np.abs(error))]
        # error_history = []
        # error_history.append(np.average(np.abs(error)))
        # print(error_history)
        # e =  error.append(np.average(np.abs(error)))

        d_predicted_output = error * sigmoid_derivative(predicted_output)

        error_hidden_layer = d_predicted_output.dot(output_weights.T)

        d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

        # Updating Weights and Biases
        output_weights += hidden_layer_output.T.dot(d_predicted_output) * lr
        output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
        hidden_weights += inputs.T.dot(d_hidden_layer) * lr
        hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr

    print("Final hidden weights: ", end='')
    print(*hidden_weights)
    print("Final hidden bias: ", end='')
    print(*hidden_bias)
    print("Final output weights: ", end='')
    print(*output_weights)
    print("Final output bias: ", end='')
    print(*output_bias)

    print("\nOutput from neural network after 10,000 epochs: ", end='')
    print(*predicted_output)
    plt.figure(figsize=(15, 5))
    plt.plot(epoch_list, error_history)
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.show()


def XOR():
    # global epoch_list, error_history

    global epoch_list, error_history

    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(x):
        return x * (1 - x)

    # Input datasets
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    expected_output = np.array([[0], [1], [1], [0]])

    epochs = 20000
    lr = 0.8
    inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons = 2, 2, 1

    # Random weights and bias initialization
    hidden_weights = np.random.uniform(size=(inputLayerNeurons, hiddenLayerNeurons))
    hidden_bias = np.random.uniform(size=(1, hiddenLayerNeurons))
    output_weights = np.random.uniform(size=(hiddenLayerNeurons, outputLayerNeurons))
    output_bias = np.random.uniform(size=(1, outputLayerNeurons))

    print("Initial hidden weights: ", end='')
    print(*hidden_weights)
    print("Initial hidden biases: ", end='')
    print(*hidden_bias)
    print("Initial output weights: ", end='')
    print(*output_weights)
    print("Initial output biases: ", end='')
    print(*output_bias)
    epoch_list = []
    error_history = []
    # Training algorithm

    for j in range(epochs):
        # Forward Propagation
        hidden_layer_activation = np.dot(inputs, hidden_weights)
        hidden_layer_activation += hidden_bias
        hidden_layer_output = sigmoid(hidden_layer_activation)

        output_layer_activation = np.dot(hidden_layer_output, output_weights)
        output_layer_activation += output_bias
        predicted_output = sigmoid(output_layer_activation)

        # Backpropagation

        epoch_list.append(j)
        # print(epoch_list)

        error = expected_output - predicted_output

        error_history.append(np.average(np.abs(error)))
        # print(error_history)
        # e =  error.append(np.average(np.abs(error)))

        d_predicted_output = error * sigmoid_derivative(predicted_output)

        error_hidden_layer = d_predicted_output.dot(output_weights.T)

        d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

        # Updating Weights and Biases
        output_weights += hidden_layer_output.T.dot(d_predicted_output) * lr
        output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
        hidden_weights += inputs.T.dot(d_hidden_layer) * lr
        hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr

    print("Final hidden weights: ", end='')
    print(*hidden_weights)
    print("Final hidden bias: ", end='')
    print(*hidden_bias)
    print("Final output weights: ", end='')
    print(*output_weights)
    print("Final output bias: ", end='')
    print(*output_bias)
    # print(epoch_list)
    # print(epoch_list)
    # print(error_history[2])

    print("\nOutput from neural network: ", end='')
    print(*predicted_output)
    plt.figure(figsize=(15, 5))
    plt.plot(epoch_list, error_history)
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.show()


print("OR Data: \n")
OR()
print("\n\nAND Data: \n")
AND()
print("\n\nXOR Data: \n")
XOR()
