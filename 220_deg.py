import numpy as np

A = np.zeros(shape=(2, 2))
u_prime = np.zeros(shape=(2, 1))
xc = 496.229473
#xc = 497.132823
yc = 396.894708
#yc = 392.351091
A[0] = [1.000886, 0.000256]
#A[0] = [1.001730, -0.026890]
A[1] = [0.000013, 1]
#A[1] = [0.065134, 1]
u_prime[0] = 495.8 - xc
u_prime[1] = 104 - yc
u_prime_prime = np.matmul(np.linalg.inv(A), u_prime)
print(u_prime_prime)
print(u_prime_prime.shape)
rho = np.sqrt(u_prime_prime[0]**2 + u_prime_prime[1]**2)
f = -2.103077e+02 + 1.474366e-03 * rho**2 + -2.739284e-06 * rho**3 + 9.964161e-09 * rho**4
#f = -2.084681e+02 + 1.344916e-03 * rho**2 - 1.823312e-06 * rho**3 + 8.398796e-09 * rho**4
rad = np.arctan2(-f, rho)
print(f)
print(np.rad2deg(rad))
print((74.5 - 2.2) / np.tan(rad))