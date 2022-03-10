import numpy as np
import math
import matplotlib.pyplot as plt

size = 5
verbose = False

GausianElimantion = True
GausianJordanElimination = True

if GausianElimantion:
    print(f"Gaussian Elimination\n")
    deviations = []
    qs = []

    for q in np.arange(0.2, 5.0, 0.15):
        q = round(q, 2)
        solution = np.zeros(size)

        backup_matrix = [
                    [2*q*pow(10, -4), 1, 6, 9, 10, 10],
                    [2*pow(10, -4), 1, 6, 9, 10, 2],
                    [1,6,6,8,6,9],
                    [5,9,10,7,10, 9],
                    [3,4,9,7,9, 3]
                        ]

        matrix_A = [
                    [2*q*pow(10, -4), 1, 6, 9, 10, 10],
                    [2*pow(10, -4), 1, 6, 9, 10, 2],
                    [1,6,6,8,6,9],
                    [5,9,10,7,10, 9],
                    [3,4,9,7,9, 3]
                    ]

        #Gausian Elimantion:
        for i in range(size):
            for j in range(i+1, size):
                l = matrix_A[j][i]/matrix_A[i][i]
                for k in range(0, size + 1):
                    matrix_A[j][k] = matrix_A[j][k] - l * matrix_A[i][k]


        if verbose:
            for row in matrix_A:
                print(f"{row}")
            print("\n", "#" * 40, "\n")


        solution[size-1] = matrix_A[size-1][size] / matrix_A[size-1][size-1]

        for i in range(size-2,-1,-1):
            solution[i] = matrix_A[i][size]
            for j in range(i+1,size):
                solution[i] = solution[i] - matrix_A[i][j]*solution[j]
            solution[i] = solution[i] / matrix_A[i][i]

        sum = 0
        for i in range(size):
            c = 0
            for j in range(size):
                c += backup_matrix[i][j] * solution[j]
            sum += math.pow(c - backup_matrix[i][size], 2) 
        deviation = math.sqrt(sum) / size 

        qs.append(q)
        deviations.append(deviation)
        print(f"For q = {q} deviation o(q) = {deviation}")

    plt.plot(qs, deviations)
    plt.xlabel("q")
    plt.ylabel("deviation")
    plt.show()

if GausianJordanElimination:
    print(f"\nGaussian-Jordan Elimination\n")
    deviations = []
    qs = []


    for q in np.arange(0.2, 5.0, 0.15):
        q = round(q, 2)
        solution = np.zeros(size)

        backup_matrix = [
                    [2*q*pow(10, -4), 1, 6, 9, 10, 10],
                    [2*pow(10, -4), 1, 6, 9, 10, 2],
                    [1,6,6,8,6,9],
                    [5,9,10,7,10, 9],
                    [3,4,9,7,9, 3]
                        ]

        matrix_A = [
                    [2*q*pow(10, -4), 1, 6, 9, 10, 10],
                    [2*pow(10, -4), 1, 6, 9, 10, 2],
                    [1,6,6,8,6,9],
                    [5,9,10,7,10, 9],
                    [3,4,9,7,9, 3]
                    ]

        for i in range(size):

            temp1 = matrix_A[i][i]

            for k in range(size + 1):
                matrix_A[i][k] =matrix_A[i][k] / temp1

            for j in range(size):
                if i != j:
                    temp2= matrix_A[j][i]

                    for k in range(size+1):
                        matrix_A[j][k] = matrix_A[j][k] - temp2 * matrix_A[i][k]


        for i in range(size):
            solution[i] = matrix_A[i][size]/matrix_A[i][i]

        sum = 0
        for i in range(size):
            c = 0
            for j in range(size):
                c += backup_matrix[i][j] * solution[j]
            sum += math.pow(c - backup_matrix[i][5], 2)

        deviation = math.sqrt(sum) / size 

        qs.append(q)
        deviations.append(deviation)
        print(f"For q = {q} deviation o(q) = {deviation}")

    plt.plot(qs, deviations)
    plt.xlabel("q")
    plt.ylabel("deviation")
    plt.show()
