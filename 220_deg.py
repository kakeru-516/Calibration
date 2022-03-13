import numpy as np

A = np.zeros(shape=(2, 2))
u_prime = np.zeros(shape=(2, 1))
xc = 495.569649
yc = 393.263400
A[0] = [0.998486, 0.000748]
A[1] = [0.002619, 1]
u_prime[0] = 495.8 - xc
u_prime[1] = 104 - yc
u_prime_prime = np.matmul(np.linalg.inv(A), u_prime)
print(u_prime_prime)
print(u_prime_prime.shape)
rho = np.sqrt(u_prime_prime[0]**2 + u_prime_prime[1]**2)
f = -2.090223e+02 + 1.657185e-03 * rho**2 + -4.161070e-06 * rho**3 + 1.253430e-08 * rho**4
rad = np.arctan2(-f, rho)
print(f)
print(np.rad2deg(rad))
print((74.5 - 2.2) / np.tan(rad))