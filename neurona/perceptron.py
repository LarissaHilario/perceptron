import csv
import random
import numpy as np
import matplotlib.pyplot as plt 

def read_data(name_file):
    matrix_data = []
    y_desired = []
    with open(name_file, 'r') as file_csv:
        reader_csv = csv.reader(file_csv, delimiter=';')
        for row in reader_csv:
            row_numbers = [float(number) for number in row[:-1]]
            matrix_data.append(row_numbers)
            y_desired.append(int(row[-1]))
    # Address VisibleDeprecationWarning:
    matrix_data = np.array(matrix_data, dtype=object)
    return matrix_data, y_desired, np.insert(np.array(matrix_data), 0, 1, axis=1)


def create_weights(num_weights):
    return [random.uniform(0, 1) for _ in range(num_weights)]

def step_function(x):
    return np.where(x >= 0, 1, 0)

def perceptron_output(features, weights, bias):
    u = np.dot(features, weights) + bias
    y_calculada = step_function(u)
    return u, np.array(y_calculada)

def calculate_delta(learning_rate, error_y, features):
    error_y_array = np.array(error_y).reshape(-1, 1)
    return learning_rate * np.dot(error_y_array.T, features)

def plot_weights_evolution(weights_evolution, epochs):
    
    num_weights = len(weights_evolution[0][0])  # Número de pesos
    num_epochs = len(weights_evolution)  # Número de épocas

    plt.figure(figsize=(10, 6))

    for i in range(num_weights):
        # Extraer los valores de peso i para todas las épocas
        weights_list = [epoch[0][i] if isinstance(epoch[0], (list, np.ndarray)) else epoch[i] for epoch in weights_evolution]
        plt.plot(range(1, num_epochs + 1), weights_list, label=f'W{i}', marker='o')

    plt.title('Evolución de los Pesos a lo largo de las Épocas')
    plt.xlabel('Épocas')
    plt.ylabel('Valor del Peso')
    plt.legend()
    plt.grid(True)
    plt.show()


def update_weights(weights, delta_weights):
    return weights + delta_weights


def run_perceptron(matrix_data, y_desired, matrix_data_w0, epochs, learning_rate):
    bias = 1
    error_norms = []
    u_values = []
    y_calculadas = []
    weights_evolution = []

    print(learning_rate)

    for epoch in range(epochs):
        error_y = []
        print(f"\nEpoch {epoch + 1}:")
        print(epoch)

        if epoch == 0:
            weights = [create_weights(len(matrix_data_w0[0]))]
            first_row_as_array = np.array(weights)
            weights_evolution.append(first_row_as_array)
        else:
            weights = np.vstack([weights, np.transpose(weights[-1])])

        for i in range(len(matrix_data_w0)):
            u, y_calculada = perceptron_output(matrix_data_w0[i], weights[epoch], bias)
            y_calculada = np.array(y_calculada)
            error = y_desired[i] - y_calculada
            error_norm = np.linalg.norm(error)
            u_values.append(u)
            y_calculadas.append(y_calculada)
            error_y.append(error)

            print(f"Conjunto de datos {i + 1}:")
            print("  Entradas:", matrix_data_w0[i])
            print("  Pesos:", weights[epoch])
            print("  y calculada:", y_calculada)
            print("  Error:", error)
            print("  Norma del error:", error_norm)
            print(f"  Suma de u para el conjunto {i + 1}: {u}")

        delta_weights = calculate_delta(learning_rate, error_y, matrix_data_w0)
        print("  Delta Weights:", delta_weights)

        weights = update_weights(weights, delta_weights)
        print("Nuevos pesos ", weights[-1])

        if epoch != epochs - 1:  
            weights_evolution.append(weights[-1]) 

        bias += learning_rate * np.sum(error_y)

        error_norms.append(np.linalg.norm(error_y))  
        print(np.linalg.norm(error_y))


    # Gráfica de la evolución del error 
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, epochs + 1), error_norms, marker='o')
    plt.title('Evolución del Error a lo largo de las Épocas')
    plt.xlabel('Épocas')
    plt.ylabel('Norma del Error')
    plt.grid(True)
    plt.show()
    
    plot_weights_evolution(weights_evolution, epochs)

    print("Sesgo final:", bias)

