a_0 = 16 + 8j
a_1 = -20 + 14j
a_2 = 4 - 8j
a_3 = -4 + 1j
a_4 = 1 + 0j

vector_a = [a_0, a_1, a_2, a_3, a_4]
alpha_max = 10e-10
IT_MAX = 20
N = 4
z0 = 5 + 5j
z1 = 5.1 + 5.1j

def calculate_b(A, z):
  b = [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j]
  for i in range (1, 5):
    b[4 - i] = A[-i] + z * b[-i]
  return b

def calculate_R(A, z):
    return A[0] + z*calculate_b(vector_a, z)[0]

def calculate_z(current_z, previous_z, current_R, previous_R):
    return current_z - (current_R*(current_z - previous_z) / (current_R - previous_R))

for l in range(1, N + 1):
  z = [0 +0j, 0 +0j, 0 +0j] #z[0] previous, z[1] current, z[2] next
  r = [0 +0j, 0 +0j, 0 +0j] #r[0] previous, r[1] current, r[2] next
  iterations = 0
  for j in range(IT_MAX):

    iterations = j
    if(j == 0):
      z[0] = z0
      z[1] = z1
      r[0] = calculate_R(vector_a, z[0])
      r[1] = calculate_R(vector_a, z[1])

    z[2] = calculate_z(z[1], z[0], r[1], r[0])
    r[2] = calculate_R(vector_a, z[2])

    if(abs(z[2] - z[1]) < alpha_max): break

    z[0] = z[1]
    z[1] = z[2]
    r[0] = r[1]
    r[1] = r[2]

  vector_a = calculate_b(vector_a, z[1])

  print(f"{l}: Re: {z[1].real}, : Im: {z[1].imag}, Iterations : {iterations}")