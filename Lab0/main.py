import numpy as np

rows = 5
columns = 5
verbose = False

GausianElimantion = False
GausianJordanElimination = True

if GausianElimantion:
    for q in np.arange(0.2, 1.0, 0.15):
        solution = np.zeros(rows)

        matrix_A = [
                    [2*q*pow(10, -4), 1, 6, 9, 10, 10],
                    [2*pow(10, -4), 1, 6, 9, 10, 2],
                    [1,6,6,8,6,9],
                    [5,9,10,7,10, 9],
                    [3,4,9,7,9, 3]
                    ]

        #Eliminacja Gaussa:
        for i in range(rows):

            for j in range(i+1, columns):
                l = matrix_A[j][i]/matrix_A[i][i]

                for k in range(columns + 1):
                    matrix_A[j][k] = round(matrix_A[j][k] - l * matrix_A[i][k], 3)


        if verbose:
            for row in matrix_A:
                print(f"{row}")
            print("\n", "#" * 40, "\n")

        #Cofanie się od ostatniego rzędu i wylia czanie wyników:
        #Wyliczam pierwszy "na sztywno" żeby móc potem z niego korzystać
        solution[rows-1] = matrix_A[rows-1][columns]/matrix_A[rows-1][rows-1]

        for i in range(rows-2,-1,-1):
            solution[i] = matrix_A[i][rows]
            
            for j in range(i+1,rows):
                solution[i] = solution[i] - matrix_A[i][j]*solution[j]
            
            solution[i] = solution[i]/matrix_A[i][i]

        print(solution)

if GausianJordanElimination:
    q = 0.2
    solution = np.zeros(rows)

    matrix_A = [
                [2*q*pow(10, -4), 1, 6, 9, 10, 10],
                [2*pow(10, -4), 1, 6, 9, 10, 2],
                [1,6,6,8,6,9],
                [5,9,10,7,10, 9],
                [3,4,9,7,9, 3]
                ]