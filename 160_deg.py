import numpy as np

A = np.zeros(shape=(2, 2))
u_prime = np.zeros(shape=(2, 1))
xc = 534.636171
#xc = 534.307309
yc = 414.713265
#yc = 414.547147
A[0] = [0.999661, 0.000161]
#A[0] = [0.999382, -0.065000]
A[1] = [0.000027, 1]
#A[1] = [0.065134, 1]
u_prime[0] = 1006.1 - xc
u_prime[1] = 414.5 - yc
u_prime_prime = np.matmul(np.linalg.inv(A), u_prime)
print(u_prime_prime)
print(u_prime_prime.shape)
rho = np.sqrt(u_prime_prime[0]**2 + u_prime_prime[1]**2)
f = -4.914462e+02 + 7.874511e-04 * rho**2 + -2.720765e-07 * rho**3 + 7.946885e-10 * rho**4
#f = -4.895800e+02 + 7.961486e-04 * rho**2 + -2.898520e-07 * rho**3 + 8.131621e-10 * rho**4
rad = np.arctan2(f, rho)
print(f)
print(np.rad2deg(rad))
print((74.5 - 2.2) / np.tan(rad))