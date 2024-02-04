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

def read_data(name_file):
    global matrix_data, weights
    matrix_data = []  
    with open(name_file, 'r') as file_csv:
        reader_csv = csv.reader(file_csv, delimiter=';')
        for row in reader_csv:
            row_numbers = [float(number) for number in row[:-1]]  
            matrix_data.append(row_numbers)
            y_desired.append(int(row[-1]))
            entry_weights = create_weights(len(row))
            weights.append(entry_weights)
    matrix_data_w0 = np.insert(np.array(matrix_data), 0, 1, axis=1)
    
    return matrix_data, y_desired, weights, matrix_data_w0


def create_weights(num_weights):
    return [1] + [random.uniform(0, 1) for _ in range(num_weights - 1)]

def step_function(x):
    return np.where(x >= 0, 1, 0)

def perceptron_output(features, weights, bias):
    print("Dimensiones de features:", features.shape)
    print("Dimensiones de weights:", np.array(weights).shape)
    
    if len(features) != len(weights):
        weights = np.transpose(weights)
        print("se transpuso")

    u = np.dot(features, weights) + bias
    y_calculada = step_function(u)
    
    return u, y_calculada

name_file = './data/E2.csv'
matrix_data, y_desired, weights, matrix_data_w0 = read_data(name_file)

for epoch in range(epochs):
    print(f"\nEpoch {epoch + 1}:")
    for i in range(len(matrix_data_w0)):
        u, y_calculada = perceptron_output(matrix_data_w0[i], weights[epoch], bias)
        error = y_desired[i] - y_calculada
        error_norm = np.linalg.norm(error)
        u_values.append(u)
        y_calculadas.append(y_calculada)
        error_norms.append(error_norm)

        print(f"Conjunto de datos {i + 1}:")
        print("  Entradas:", matrix_data_w0[i])
        print("  Pesos:", weights[epoch])
        print("  u:", u)
        print("  y calculada:", y_calculada)
        print("  Error:", error)
        print("  Norma del error:", error_norm)

print("\nPesos finales:")
for epoch, peso in enumerate(weights):
    print(f"Iteración {epoch + 1}: {peso}")

print("Sesgo final:", bias)
