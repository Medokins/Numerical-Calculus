import numpy as np

size = 5
verbose = False

GausianElimantion = False
GausianJordanElimination = True

if GausianElimantion:
    for q in np.arange(0.2, 1.0, 0.15):
        solution = np.zeros(size)

        matrix_A = [
                    [2*q*pow(10, -4), 1, 6, 9, 10, 10],
                    [2*pow(10, -4), 1, 6, 9, 10, 2],
                    [1,6,6,8,6,9],
                    [5,9,10,7,10, 9],
                    [3,4,9,7,9, 3]
                    ]

        #Eliminacja Gaussa:
        for i in range(size):

            for j in range(i+1, size):
                l = matrix_A[j][i]/matrix_A[i][i]

                for k in range(size + 1):
                    matrix_A[j][k] = round(matrix_A[j][k] - l * matrix_A[i][k], 3)


        if verbose:
            for row in matrix_A:
                print(f"{row}")
            print("\n", "#" * 40, "\n")

        #Cofanie się od ostatniego rzędu i wylia czanie wyników:
        #Wyliczam pierwszy "na sztywno" żeby móc potem z niego korzystać
        solution[size-1] = matrix_A[size-1][size]/matrix_A[size-1][size-1]

        for i in range(size-2,-1,-1):
            solution[i] = matrix_A[i][size]
            
            for j in range(i+1,size):
                solution[i] = solution[i] - matrix_A[i][j]*solution[j]
            
            solution[i] = solution[i]/matrix_A[i][i]

        print(solution)

if GausianJordanElimination:
    for q in np.arange(0.2, 5.0, 0.15):
        solution = np.zeros(size)

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
                        matrix_A[j][k] = round(matrix_A[j][k] - temp2 * matrix_A[i][k], 5)


        for i in range(size):
            solution[i] = matrix_A[i][size]/matrix_A[i][i]

        print(solution)