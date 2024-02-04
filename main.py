import csv
import random
import numpy as np

matrix_data = []
y_desired = []
weights = []
learning_rate = 1
epochs = 4
bias = 1
error_norms = []
u_values = []
y_calculadas = []

name_file = './data/E2.csv'

def read_data(name_file):
    global matrix_data, weights
    matrix_data = []  
    with open(name_file, 'r') as file_csv:
        reader_csv = csv.reader(file_csv, delimiter=';')
        for row in reader_csv:
            row_numbers = [float(number) for number in row[:-1]]  
            matrix_data.append(row_numbers)
            y_desired.append(int(row[-1]))
            entry_weights = create_weights(np.array(matrix_data).shape[1] + 1)
            weights.append(entry_weights)
    matrix_data_w0 = np.insert(np.array(matrix_data), 0, 1, axis=1)
    return matrix_data, y_desired, weights, matrix_data_w0

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


matrix_data, y_desired, weights, matrix_data_w0 = read_data(name_file)

for epoch in range(epochs):
    error_y = []  
    print(f"\nEpoch {epoch + 1}:")
    for i in range(len(matrix_data_w0)):
        u, y_calculada = perceptron_output(matrix_data_w0[i], weights[epoch], bias)
        y_calculada = np.array(y_calculada)
        error = y_desired[i] - y_calculada
        error_norm = np.linalg.norm(error)
        u_values.append(u)
        y_calculadas.append(y_calculada)
        error_y.append(error)
        error_norms.append(error_norm)
        
        print(f"Conjunto de datos {i + 1}:")
        print("  Entradas:", matrix_data_w0[i])
        print("  Pesos:", weights[epoch])
        print("  y calculada:", y_calculada)
        print("  Error:", error)
        print("  Norma del error:", error_norm)
        print(f"  Suma de u para el conjunto {i + 1}: {u}")
        
    delta_weights = calculate_delta(learning_rate, error_y, matrix_data_w0)
    print("  Delta Weights:", delta_weights)

    weights[epoch] += delta_weights  
    print("Nuevos pesos ", weights[epoch])
    bias += learning_rate * np.sum(error_y)

print("Sesgo final:", bias)
